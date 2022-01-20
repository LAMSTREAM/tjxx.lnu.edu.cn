import os
import time
import datetime
import pickle
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

path = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'

class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

class Solution:

    liudong0 = "/html/body/div[1]/form/div[3]/div[2]/label[1]"
    liudong1 = "/html/body/div[1]/form/div[3]/div[2]/label[2]"
    liudong2 = "/html/body/div[1]/form/div[3]/div[2]/label[3]"
    jiechu0 = "/html/body/div[1]/form/div[4]/div[2]/label[1]"
    jiechu1 = "/html/body/div[1]/form/div[4]/div[2]/label[2]"
    tiwen = "/html/body/div[1]/form/div[5]/div[2]/div[1]/input"
    zhenzhuang0 = "/html/body/div[1]/form/div[6]/div[2]/label[1]"
    zhenzhuang1 = "/html/body/div[1]/form/div[6]/div[2]/label[2]"
    zhenzhuang2 = "/html/body/div[1]/form/div[6]/div[2]/label[3]"
    guancha0 = "/html/body/div[1]/form/div[7]/div[2]/label[1]"
    guancha1 = "/html/body/div[1]/form/div[7]/div[2]/label[2]"
    guancha2 = "/html/body/div[1]/form/div[7]/div[2]/label[3]"
    guancha3 = "/html/body/div[1]/form/div[7]/div[2]/label[4]"
    zaigang0 = "/html/body/div[1]/form/div[8]/div[2]/label[1]"
    zaigang1 = "/html/body/div[1]/form/div[8]/div[2]/label[2]"
    zaigang2 = "/html/body/div[1]/form/div[8]/div[2]/label[3]"
    zaigang3 = "/html/body/div[1]/form/div[8]/div[2]/label[4]"
    guiji0 = "/html/body/div[1]/form/div[9]/div[2]/label[1]"
    guiji1 = "/html/body/div[1]/form/div[9]/div[2]/label[2]"
    submit = "/html/body/div[1]/form/div[10]/a"
    confirmsubmit = "/html/body/div[3]/div[2]/div[2]/a[2]"

    def __init__(self,path,headlessbool):
        try:
            options = Options()
            if headlessbool:
                options.headless = True
            else:
                options.headless = False
            self.driver = webdriver.Chrome(options=options, executable_path=path)
        except:
            raise(MyError('initialize error'))

    def geturl(self):
        try:
            url = "https://tjxx.lnu.edu.cn"
            self.driver.get(url)
        except:
            raise(MyError('fail to connect website'))

    def finish(self):
        try:
            self.driver.find_element_by_xpath(self.liudong0).click()
            self.driver.find_element_by_xpath(self.jiechu0).click()
            self.driver.find_element_by_xpath(self.zhenzhuang0).click()
            self.driver.find_element_by_xpath(self.guancha0).click()
            self.driver.find_element_by_xpath(self.zaigang0).click()
            self.driver.find_element_by_xpath(self.guiji0).click()

            tempre = self.driver.find_element_by_xpath(self.tiwen)
            tempre.clear()
            tempre.send_keys("37")
            tempre.send_keys(Keys.RETURN)

            time.sleep(1)
            self.driver.find_element_by_xpath(self.submit).click()
            time.sleep(5)
            self.driver.find_element_by_xpath(self.confirmsubmit).click()
            time.sleep(1)
        except:
            raise(MyError('fail to finish upload'))

    def savecookie(self):
        pickle.dump(self.driver.get_cookies(), open("cookies.pkl", "wb"))

    def readcookie(self):
        try:
            cookies = pickle.load(open("cookies.pkl", "rb"))
            for cookie in cookies:
                self.driver.add_cookie(cookie)
        except:
            raise(MyError('read Cookie error'))

    def do(self):
        try:
            # use cookie to login
            self.geturl()
            self.readcookie()
            self.geturl()

            # input imf
            self.finish()
            self.savecookie()
            self.driver.close()

            print('success')
        except MyError as me:
            print(me.value)

if __name__ == '__main__':
    while True:
        recenttime = int(datetime.datetime.now().strftime('%H%M'))
        if 700 < recenttime < 800:
            sol = Solution(path, True)
            sol.do()
            time.sleep(23*60)
        else:
            time.sleep(600)
