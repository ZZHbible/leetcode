import json
import os.path
from collections import defaultdict
from time import sleep

import requests
from pyquery import PyQuery as pq
from selenium import webdriver
import schedule


def crawl_weibo(save_path_json):
    prew_key = {}
    if os.path.exists(save_path_json):
        with open(save_path_json, 'r', encoding='utf-8') as f:  # 先从json文本中读取已存在的项目
            if os.path.getsize(save_path_json) > 0:  # 判断文件是否为空
                prew_key = json.load(f)
    print(len(prew_key))
    option = webdriver.ChromeOptions()
    option.add_argument("headless")  # 不打开浏览器
    url = "https://s.weibo.com/top/summary?cate=realtimehot"
    driver = webdriver.Chrome(executable_path='/Users/zhangzhenhua/Downloads/chromedriver', options=option)
    driver.get(url=url)
    sleep(10)  # 等待服务器相应

    docs = pq(driver.page_source)
    content_dict = defaultdict(str)
    for link in docs('td.td-02 a'):  # 查找属性
        if link.text not in prew_key:  # 去重
            content_dict[link.text] = "https://s.weibo.com" + link.items()[0][1]
    prew_key.update(content_dict)
    with open(save_path_json, "w+") as f:
        f.write(json.dumps(prew_key, ensure_ascii=False))
    # print(docs)
    driver.quit()


def task():  # 定时任务，可以用系统自带取代
    schedule.clear()
    schedule.every(10).seconds.do(crawl_weibo, save_path_json='./weibo.json')  # 每10s运行一次

    while True:
        schedule.run_pending()
        sleep(1)


task()
# crawl_weibo('./weibo.json')
