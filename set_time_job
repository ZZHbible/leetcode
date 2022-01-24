import datetime
import os
import json

from apscheduler.schedulers.blocking import BlockingScheduler


def statistic_model():
    with open('record_everyday.log', 'a+') as f:
        try:
            status = os.system("/Users/zhangzhenhua/.conda/envs/py39/bin/python" + " -m nestser.query")
            if status == 0:
                ret = os.popen("/Users/zhangzhenhua/.conda/envs/py39/bin/python" + " -m nestser.query").read()

                log_dict ={}
                ret = json.dumps(ret.replace('\n', '').replace(' ', ''))
                index = 0
                flag = 0  # 0 表示success, 1 表示compute, 2 表示queue
                while ret.find('{count:', index) != -1:
                    index = ret.find('{count:', index)
                    index += 7
                    num = ""
                    while ret[index].isdigit():
                        num += ret[index]
                        index += 1
                    num = int(num)
                    if flag == 0:
                        log_dict["success"] = num
                    elif flag == 1:
                        log_dict["compute"] = num
                    elif flag == 2:
                        log_dict["queue"] = num
                    flag += 1
                    index = index + 1

                print(json.dumps(log_dict))

                # 获取当前时间
                now_time = datetime.datetime.now()

                log_dict["date"]=now_time.strftime("%Y-%m-%d")

                f.write(json.dumps(log_dict)+'\n')
            else:
                print("some wrong")
        except IOError:
            print("IOError")


def dojob():
    # 创建调度器：BlockingScheduler
    scheduler = BlockingScheduler()

    now = datetime.datetime.now()
    zero_today = now - datetime.timedelta(hours=now.hour, minutes=now.minute, seconds=now.second,
                                          microseconds=now.microsecond)
    last_today = zero_today + datetime.timedelta(hours=23, minutes=59, seconds=59)

    # 添加任务,时间间隔5S
    scheduler.add_job(statistic_model, 'interval', hours=24, start_date=last_today, id='test_job2')
    scheduler.start()


dojob()

print(datetime.datetime.now())
