#!/usr/bin/env python
# author = 'ZZH'
# time = 2023/8/2
# project = 量化回测demo

from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
from numpy import int64
import glob
from tqdm import tqdm

dtype = [(item, float) for item in
         ['timestamp', 'open', 'high', 'low', 'close', 'volume', 'notional', 'buy_volume', 'buy_notional',
          'sell_volume', 'sell_notional', 'bid_price', 'bid_volume', 'ask_volume', 'ask_price', 'last_traded_price',
          'last_traded_volume', 'system_timestamp']]

def mean_reversion_strategy(data: pd.DataFrame, window=5, deviation=0.5):
    # 计算均值
    data['mean'] = data['close'].rolling(window=window).mean()

    # 计算价格与均值的偏离
    data['deviation'] = (data['close'] - data['mean']) / data['mean']

    # 生成交易信号
    data['signal'] = 0
    data.loc[data['deviation'] > deviation, 'signal'] = -1  # 偏离过高，卖出信号
    data.loc[data['deviation'] < -deviation, 'signal'] = 1  # 偏离过低，买入信号

    # 计算每次交易的收益
    data['returns'] = data['signal'].shift() * data['close'].pct_change()

    # 计算累积收益
    data['cumulative_returns'] = (1 + data['returns']).cumprod()

    return data


def moving_average_crossover_strategy(data: pd.DataFrame, short_window=5, long_window=20):
    # 计算短期均线和长期均线
    data['short_ma'] = data['close'].rolling(window=short_window).mean()
    data['long_ma'] = data['close'].rolling(window=long_window).mean()

    # 生成交易信号
    data['signal'] = 0
    data.loc[data['short_ma'] > data['long_ma'], 'signal'] = 1  # 短期均线从下方穿过长期均线，买入信号
    data.loc[data['short_ma'] < data['long_ma'], 'signal'] = -1  # 短期均线从上方穿过长期均线，卖出信号

    # 计算每次交易的收益
    data['returns'] = data['signal'].shift() * data['close'].pct_change()

    # 计算累积收益
    data['cumulative_returns'] = (1 + data['returns']).cumprod()

    return data


def convert_tick_to_kline(tick_data, kline_interval='5T'):
    # 将时间戳转换为pandas的DatetimeIndex，并设置为索引
    tick_data['timestamp'] = pd.to_datetime(tick_data['timestamp'], unit='ms')
    tick_data.set_index('timestamp', inplace=True)

    # 以指定的k线周期（5分钟）对tick数据进行重新采样
    kline_data = tick_data['close'].resample(kline_interval).ohlc()
    kline_data['volume'] = tick_data['volume'].resample(kline_interval).sum()

    return kline_data


def my_strategy(data: pd.DataFrame, rate=0.0005):
    data['rate'] = data['close'].pct_change()
    data['signal'] = None
    data.loc[data['rate'] > rate, 'signal'] = 1
    data.loc[data['rate'] < -rate, 'signal'] = -1

    data['signal'] = data['signal'].replace(None, method='ffill')

    # 计算每次交易的收益
    data['returns'] = data['signal'].shift() * data['close'].pct_change()

    # 计算累积收益
    data['cumulative_returns'] = (1 + data['returns']).cumprod()
    return data

def calculate_metrics(trades):
    total_trades = len(trades)

    if total_trades == 0:
        return {
            'profit_rate': 0.0,
            'win_rate': 0.0,
            'profit_loss_ratio': 0.0,
            'num_trades': 0,
            'sharpe_ratio': 0.0
        }

    # Calculate profit for each trade
    profits = [(trade['exit_price'] - trade['entry_price']) for trade in trades]

    # Calculate metrics
    total_profit = sum(profits)
    win_trades = sum(1 for p in profits if p > 0)
    loss_trades = total_trades - win_trades
    win_rate = win_trades / total_trades
    profit_loss_ratio = sum(p for p in profits if p > 0) / abs(sum(p for p in profits if p < 0))
    profit_rate = total_profit / total_trades
    avg_profit_per_trade = total_profit / total_trades
    std_dev = np.std(profits)
    sharpe_ratio = (avg_profit_per_trade / std_dev) if std_dev != 0 else 0.0

    metrics = {
        'profits': sum(profits),
        'profit_rate': profit_rate,
        'win_rate': win_rate,
        'profit_loss_ratio': profit_loss_ratio,
        'num_trades': total_trades,
        'sharpe_ratio': sharpe_ratio
    }

    return metrics

# Usage example:
# Assuming 'trades' is the list of trades obtained from the backtesting process.
# metrics = calculate_metrics(trades)
# print(metrics)


def calc(result_datas):
    total_trades=[]
    for result_data in result_datas:

        # 输出交易记录
        trades = []
        current_position = 0
        for index, row in result_data.iterrows():
            if row['signal'] == 1 and current_position == 0:  # 买入信号且当前没有持仓
                entry_price = row['close']
                entry_time = index
                current_position = 1
            elif row['signal'] == -1 and current_position == 1:  # 卖出信号且当前持仓
                exit_price = row['close']
                exit_time = index
                trades.append({
                    'entry_time': entry_time,
                    'exit_time': exit_time,
                    'entry_price': entry_price,
                    'exit_price': exit_price
                })
                current_position = 0

        total_trades.extend(trades)
        # for trade in trades:
        #     one_day_profit += (trade['exit_price'] - trade['entry_price'])
        #     # print(f"开仓时间：{trade['entry_time']}, 平仓时间：{trade['exit_time']}, 开仓价：{trade['entry_price']}, 平仓价：{trade['exit_price']}")

    # print(f"盈利价格为:{one_day_profit}")

    return calculate_metrics(total_trades)


def process_one_file(file_path, kline_interval):
    dtype[0] = ('timestamp', int64)
    dtype[-1] = ('system_timestamp', int64)
    dfs = []

    with h5py.File(file_path, 'r') as h5_file:
        # 读取数据集
        group_name = 'future_tick'  # 请替换为实际的组名
        if group_name in h5_file:
            group = h5_file[group_name]
            # Now you can read individual datasets within the group or perform other operations
            for dataset_name in group.keys():
                dataset = group[dataset_name][:]

                numpy_void_array = np.array(dataset, dtype=dtype)
                dfs.append(pd.DataFrame(numpy_void_array))

    kline_datas = [convert_tick_to_kline(df, kline_interval=kline_interval) for df in dfs]

    result_datas = [my_strategy(kline_data, )
                    for kline_data in kline_datas]

    return calc(result_datas)


def main():
    # files = glob.glob('ticks/*.h5')
    files = ['ticks/2023-07-03_today.h5', 'ticks/2023-07-04_today.h5', 'ticks/2023-07-05_today.h5',
             'ticks/2023-07-06_today.h5']
    num_files = len(files)
    kline_interval = '1T'
    import time
    t = time.time()
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(process_one_file, file, kline_interval) for file in files]

        total_num = 0
        for future in tqdm(futures, total=num_files, desc='Processing Files'):
            result = future.result()
            # result 中包含了利润率，胜率，盈亏比，交易次数，夏普值等指标,这里只列出了盈利情况
            total_num += result['profits']

    print(f"总时间为{time.time() - t}")

    print(f"总盈利价格为:{total_num}")

if __name__=='__main__':
    main()
