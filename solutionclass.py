import os
import time
import datetime
import pickle
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

path = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'

def savePath(_path):
    try:
        f = open('pathway.txt', 'w')
        f.write(_path)
        f.close()
    except:
        raise (MyError('保存浏览器驱动路径失败!'))

def readPath():
    try:
        f = open('pathway.txt', 'r')
        _path = f.readline()
        f.close()
        return _path
    except:
        raise (MyError('读取浏览器驱动路径失败!'))

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
            raise(MyError('初始化失败!'))

    def geturl(self):
        try:
            url = "http://tjxx.lnu.edu.cn/inputExt.asp"
            self.driver.get(url)
        except:
            raise(MyError('链接至填报网站失败!'))

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
            raise(MyError('未能成功提交填报,请在填报时段再试!'))

    def savecookie(self):
        pickle.dump(self.driver.get_cookies(), open("cookies.pkl", "wb"))

    def readcookie(self):
        try:
            cookies = pickle.load(open("cookies.pkl", "rb"))
            for cookie in cookies:
                self.driver.add_cookie(cookie)
        except:
            raise (MyError('读取Cookie错误!'))

    def confirmCookie(self):
        time.sleep(1)
        try:
            _temp = self.driver.find_element_by_xpath(self.liudong0)
        except:
            raise MyError('未能成功以Cookie登入')

    def do(self):
        try:
            # use cookie to login
            self.geturl()
            self.readcookie()
            self.geturl()
            self.confirmCookie()

            # input imf
            self.finish()
            self.savecookie()
            self.driver.close()

            print('填报成功')
        except MyError as _er:
            print(_er.value)
            self.driver.close()
            print('自动关闭浏览器,等待状态中...')

    def subDo(self):
            # use cookie to login
            self.geturl()
            self.readcookie()
            self.geturl()
            self.confirmCookie()

            # input imf
            self.finish()
            self.savecookie()
            self.driver.close()

if __name__ == '__main__':
    sol = Solution(path, False)
    sol.do()
    while True:
        recenttime = int(datetime.datetime.now().strftime('%H%M'))
        if 700 < recenttime < 900:
            sol = Solution(path, False)
            sol.do()
            time.sleep(10*60*60)
        else:
            time.sleep(600)
