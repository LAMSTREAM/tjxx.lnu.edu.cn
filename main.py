import os
import time
import datetime
import vthread
import pyautogui
import solutionclass
from solutionclass import MyError
from solutionclass import Solution

pool_1 = vthread.pool(1,gqueue=1)
pool_2 = vthread.pool(1,gqueue=2)

@pool_1
def warningthread(_text):
    pyautogui.alert(_text)

@pool_2
def yesmain():
    while 1:
        workingMode = pyautogui.confirm(text='选择工作模式', title='lyns', buttons=['配置', '开始'])
        if(workingMode == "配置"):
            try:
                try:
                    workingPath = solutionclass.readPath()
                except:
                    workingPath = ''
                workingPath = pyautogui.prompt(text='请填入webdriver工作目录', title='lyns', default=workingPath)
                sol = Solution(workingPath,False)
                sol.geturl()
                if ('是' == pyautogui.confirm(text='完成初次登陆配置?', title='lyns', buttons=['否', '是'])):
                    sol.savecookie()
                    solutionclass.savePath(workingPath)
                    sol.driver.close()
                else:
                    sol.driver.close()
                    continue
            except MyError as _er:
                pyautogui.alert(_er.value)
        elif(workingMode == "开始"):
            try:
                workingPath = solutionclass.readPath()
            except:
                pyautogui.alert('读取浏览器驱动路径错误!')
                continue
            try:
                sol = Solution(workingPath, False)
                sol.subDo()
                warningthread('填报成功！ 待机等待下一次填报....')
            except MyError as _er:
                sol.driver.close()
                warningthread(_er.value+'  \n返回配置状态...')
                continue
            while 1:
                recenttime = int(datetime.datetime.now().strftime('%H%M'))
                if 700 < recenttime < 900:
                    try:
                        sol = Solution(workingPath, False)
                        sol.subDo()
                        time.sleep(10 * 60 * 60)
                        warningthread('填报成功！ 待机等待下一次填报....')
                    except MyError as _er:
                        sol.driver.close()
                        warningthread(_er.value+'  \n返回配置状态...')
                        break

                else:
                    time.sleep(600)
        else:
            pass
        break

for i in  range(1):yesmain()