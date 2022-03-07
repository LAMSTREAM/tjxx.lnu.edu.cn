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
    pyautogui.alert(_text, title='lyns')

@pool_2
def yesmain():
    while 1:
        workingMode = pyautogui.confirm(text='选择工作模式', title='lyns', buttons=['配置', '开始', '待机'])
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
                if(_er.value == '当日填报结束'):
                    warningthread(_er.value + '  \n自动进入待机状态...')
                    sol.driver.close()
                else:
                    warningthread(_er.value+'  \n返回配置状态...')
                    sol.driver.close()
                    continue
            while 1:
                recenttime = int(datetime.datetime.now().strftime('%H%M'))
                if (700 < recenttime < 900):
                    try:
                        sol = Solution(workingPath, False)
                        sol.subDo()
                        time.sleep(10 * 60 * 60)
                        warningthread('填报成功！ 待机等待下一次填报....')
                    except MyError as _er:
                        if (_er.value == '当日填报结束'):
                            warningthread(_er.value + '  \n自动进入待机状态...')
                            sol.driver.close()
                            time.sleep(600)
                        else:
                            warningthread(_er.value + '  \n返回配置状态...')
                            sol.driver.close()
                            break

                else:
                    time.sleep(600)
        elif(workingMode == "待机"):
            while 1:
                hour = datetime.datetime.now().hour
                minute = datetime.datetime.now().minute
                recenttime = hour*100 + minute
                if (700 < recenttime < 900):
                    try:
                        sol = Solution(workingPath, False)
                        sol.subDo()
                        time.sleep(10 * 60 * 60)
                        warningthread('填报成功！ 待机等待下一次填报....')
                    except MyError as _er:
                        if (_er.value == '当日填报结束'):
                            sol.driver.close()
                            warningthread(_er.value + '  \n自动进入待机状态...')
                            time.sleep(600)
                        else:
                            sol.driver.close()
                            warningthread(_er.value + '  \n返回配置状态...')
                            break

                else:
                    time.sleep(600)
        else:
            pass
        break

if __name__ == '__main__':
    yesmain()
