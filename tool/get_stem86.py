#! python3
# getXiaochengPPT.py - Automatic acquisition of Xiaocheng courseware.
#先打开截屏软件snagit caption,设置fixed region
#文件夹中需要ppt模板文件ai00
#使用mouseNow.py程序获取鼠标需要点击的坐标位置
#打开需要截屏的浏览器页面https://www.stem86.com/#/teacher_ppt?slideId=1395
#

import pyautogui, time
from selenium import webdriver
from shutil import copyfile
import subprocess
import sys

pyautogui.PAUSE = 0.2

copyppt = (120,150)     #打开ppt文件，索引栏位置
chrome = (130,1065)    #任务栏chrome坐标
dos02 = (164,1065)
ppt03 = (204,1065)
chromePPT = (290,290)
pptField = (635,351)
scroll = (1911,943)
xiayixie=(1630,1008)    #网页中‘下一页’按钮

mobanPPT = 'ai00.pptx'    #模板PPT

def newPPT(filename,num):
    '''根据‘mobanPPT’复制一个ppt文件，命名为filename，复制‘num’张空白ppt。打开ppt，并且全屏'''
    copyfile(mobanPPT, filename)
    #打开ppt文件
    subprocess.Popen(['start', filename],shell=True)
    time.sleep(2)
    #点击ppt文件索引栏第一张空白PPT，复制，黏贴num次
    pyautogui.click(copyppt[0], copyppt[1])
    pyautogui.hotkey('ctrl', 'c') 
    for m in range(1,num):
        pyautogui.hotkey('ctrl', 'v') 
    time.sleep(2)
    #保存并且关闭ppt
    pyautogui.hotkey('ctrl', 's')
    pyautogui.hotkey('alt', 'f4')
    #打开ppt
    subprocess.Popen(['start', filename],shell=True)
    time.sleep(2)
    #ppt全屏
    pyautogui.hotkey('winleft','up')


#定义函数，截取某节课程网页中的内容，复制到ppt，保存并关闭ppt。
def captureToPPT(n,totalNumber):

    #准备空白的ppt文件
    filename = 'stem0{0}.pptx'.format(n)
    newPPT(filename,totalNumber)

    #点击运行python程序的dos窗口
    pyautogui.click(dos02[0], dos02[1])
    
    for number in range(1,totalNumber+1):
        # Give the user a chance to kill the script.
        pyautogui.click(dos02[0], dos02[1])
        print('>>> 1 SECOND PAUSE TO LET USER PRESS CTRL-C <<<')
        time.sleep(1)

        pyautogui.click(chrome[0], chrome[1])

        pyautogui.hotkey('alt', 'd') 
        pyautogui.click(xiayixie[0], xiayixie[1])
#        pyautogui.typewrite(['down', '\t'])
        time.sleep(1)
        pyautogui.click(ppt03[0], ppt03[1])
        pyautogui.click(pptField[0], pptField[1])
        pyautogui.hotkey('ctrl', 'v') 
        pyautogui.click(scroll[0], scroll[1])

    time.sleep(0.5)
    #保存并且关闭ppt
    pyautogui.hotkey('ctrl', 's')
    pyautogui.hotkey('alt', 'f4')
    
filename_num=input('第几章的第几课0101:')
totalNumber=int(input('本节课共几张ppt:'))
captureToPPT(filename_num,totalNumber)


