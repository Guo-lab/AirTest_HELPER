# -*- encoding=utf8 -*-
__author__ = "gsq"

from airtest.core.api import *
from poco.drivers.ios import iosPoco


auto_setup(__file__)
connect_device("ios:///127.0.0.1:8100")

poco = iosPoco()

# home()
# poco("Window").offspring("Home screen icons").child("Other").child("Other").offspring("常用")[0].click() 
# touch(Template(r"tpl1681481749960.png", record_pos=(-0.232, -0.037), resolution=(750, 1334)))

# wait(Template(r"tpl1682007164947.png", record_pos=(0.0, -0.671), resolution=(750, 1334)))

# # Ref: https://github.com/airtestproject/poco/issues/189
# # Ref2: https://github.com/AirtestProject/Poco/issues/559

# poco("发现").click()
# touch(Template(r"tpl1681479860264.png", record_pos=(0.013, -0.64), resolution=(750, 1334)))




screenWidth, screenHeight = poco.get_screen_size()
print(screenWidth, " ", screenHeight)

swipe((screenWidth * 0.5, screenHeight * 0.9), vector=[0, -0.4], duration=0.5)

sleep(1)

while True:

    # 查找评论按钮
    tableList = poco("Window").offspring("Table").offspring("Moments_OperationButton")

    
    # 点击评论按钮
    for child in tableList:
        childX, childY = child.get_position()
        if (childY >= 0.1 and childY < 1.0):
            child.click()
            if poco("赞").exists():
                poco("赞").click()
                child.click()
                continue
            if poco("Window").offspring("关闭").exists():
                poco("Window").offspring("关闭").click()

    swipe((screenWidth * 0.5, screenHeight * 0.9), vector=[0, -0.7], duration=0.5)
    
    sleep(1)

