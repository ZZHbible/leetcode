import json
from collections import defaultdict

import telebot
from selenium import webdriver
import time
from pyquery import PyQuery as pq

# get token
with open("config.json",'r',encoding='utf-8') as f:
    token = json.load(f)["token"]

bot=telebot.TeleBot(token)
option = webdriver.ChromeOptions()
option.add_argument('headless')


def extract_arg(arg):
    return arg.split()[1:]

@bot.message_handler(func=lambda message: True, content_types=['sticker', 'photo'])
def default_command(message):
    bot.reply_to(message, "This is the sticker or photo command handler.")
@bot.message_handler(commands=['weibo'])
def crawl_weibo(message):
    driver = webdriver.Chrome(executable_path="/Users/zhangzhenhua/Downloads/chromedriver", options=option)
    driver.get("https://s.weibo.com/top/summary?cate=realtimehot")
    time.sleep(10)
    docs = pq(driver.page_source)
    content_dict = defaultdict(str)
    for link in docs('td.td-02 a'):  # 查找属性
        content_dict[link.text] = "https://s.weibo.com" + link.items()[0][1]
    driver.quit()
    for i in content_dict:
        bot.send_message(message.chat.id, text="name:{},detail:{}".format(i, content_dict[i]))
@bot.message_handler(commands=['ins'])
def get_instgram_photo(message):
    from selenium.webdriver.common.keys import Keys
    def parse_arg(text):
        return text.split()[1:]
    driver = webdriver.Chrome(executable_path="/Users/zhangzhenhua/Downloads/chromedriver", options=option)
    driver.implicitly_wait(300)
    driver.get("https://www.instagram.com")
    driver.find_element_by_name("username").send_keys("ymyyyds")
    driver.find_element_by_name("password").send_keys("ymyyyds.")
    driver.find_element_by_css_selector('.sqdOP.L3NKy.y3zKF').send_keys(Keys.ENTER)
    time.sleep(3)
    names=parse_arg(message.text)
    for name in names:
        try:
            driver.get("https://www.instagram.com/"+name+'/')
            docs = pq(driver.page_source)
            for image in docs('.v1Nh3.kIKUG._bz0w a img')[:5]:
                bot.send_photo(message.chat.id, photo=image.items()[-2][1])
        except:
            bot.reply_to(message,"no photo named "+name)
    driver.quit()

@bot.message_handler(commands=['start'])
def send_welcome(message):

    bot.send_message(message.chat.id, "use command /weibo to get the weibo realtime hot  "
                                      "use command /ins namelist to get the ins photo ")

bot.polling()