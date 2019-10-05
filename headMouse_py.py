## 使用 pyautogui 模块相关函数，可以模拟鼠标及键盘操作， 完整说明文档见: http://pyautogui.readthedocs.org/
# pip install pyautogui
# 要注意的是，模拟移动鼠标与击键可能太快，导致其他程序跟不上，并且程序可能失去控制，
# 需要掌握如何从问题中恢复，至少要能中止它。
# 防止或恢复GUI自动化问题
#  1) 使用pyautogui.PAUSE设置每个PyAutoGUI函数调用在执行动作后暂停的秒数
#  2) pyautogui自动防故障功能：将鼠标移到屏幕的左上角，来抛出failSafeException异常
import pyautogui
import time
import serial

pyautogui.PAUSE=1
pyautogui.FAILSAFE=True      # 启用自动防故障功能
width,height=pyautogui.size()   # 屏幕的宽度和高度
x,y=pyautogui.position()# 鼠标当前位置
serial=serial.Serial('COM13',9600)
data=''

while True:
  print(data)
  data=serial.read()
  ## 控制鼠标移动
  if(str(data)=="b'u'"):
    y=y-100
    pyautogui.moveTo(None,y)
  data=serial.read()
  if(str(data)=="b'd'"):
    y=y+100
    pyautogui.moveTo(None,y)
  data=serial.read()
  if(str(data)=="b'l'"):
    x=x-100
    pyautogui.moveTo(x,None)
  data=serial.read()
  if(str(data)=="b'r'"):
    x=x+100
    pyautogui.moveTo(x,None)
  if(str(data)=="b'a'"):
    pyautogui.click(x=None, y=None, clicks=1, interval=0.0, button='left', duration=0.0, tween=pyautogui.linear)
  if(str(data)=="b'b'"):
    pyautogui.click(x=None, y=None, clicks=1, interval=0.0, button='right', duration=0.0, tween=pyautogui.linear)
  data=serial.read()

