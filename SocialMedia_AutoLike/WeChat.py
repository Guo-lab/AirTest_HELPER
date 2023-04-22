# -*- encoding=utf8 -*-
__author__ = "gsq"

# Reference:
# https://cloud.tencent.com/developer/article/1379155
# https://airtest.doc.io.netease.com/IDEdocs/poco_framework/3_UI_script/
# https://airtest.doc.io.netease.com/IDEdocs/poco_framework/4_poco_API/
# https://www.cnblogs.com/AirtestProject/p/14688909.html
  
from airtest.core.api import *
from airtest.cli.parser import cli_setup
import pdb # can not be used


# script content
print("start...")


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)


from poco.drivers.ios import iosPoco

auto_setup(__file__)
connect_device("ios:///127.0.0.1:8100")

poco = iosPoco()


# assert_exists(Template(r"tpl1681478902425.png", record_pos=(-0.117, -0.471), resolution=(750, 1334)), "找到微信")
# poco(Template(r"tpl1681478902425.png", record_pos=(-0.117, -0.471), resolution=(750, 1334))).click()

touch(Template(r"tpl1681479147292.png", record_pos=(-0.115, -0.491), resolution=(750, 1334)))
assert_exists(Template(r"tpl1681479164586.png", record_pos=(-0.235, -0.035), resolution=(750, 1334)), "WeChat Test.")

# poco("Window").offspring("Home screen icons").child("Other").child("Other")[2].offspring("微信").click()
touch(Template(r"tpl1681481749960.png", record_pos=(-0.232, -0.037), resolution=(750, 1334)))


sleep(3)


# poco("发现").click()
# # poco("朋友圈").click()

poco("发现").click()
touch(Template(r"tpl1681479860264.png", record_pos=(0.013, -0.64), resolution=(750, 1334)))




screenWidth, screenHeight = poco.get_screen_size()
print(screenWidth, " ", screenHeight)

while True:
    # 查找评论按钮
    tableList = poco("Table").offspring('Moments_OperationButton')
    
    # poco("Window").child("Other").child("Other").child("Other").child("Other").child("Other").child("Other").child("Other").child("Other").offspring("Table").offspring("Moments_OperationButton")[0]

    # 点击评论按钮
    for child in tableList:
        # pdb.set_trace()
        childX, childY = child.get_position()
        print(childX, " ", childY)
        if (childY >= 0.1 and childY < 1.0):
            child.click()
            if poco("赞").exists():
                poco("赞").click()
                # touch(Template(file:///Users/cengsijian/Desktop/AirTest/AirTestWeixinTest.air/tpl1545118102228.png, record_pos=(0.057, 0.385), resolution=(750, 1334)))
            else:
                continue
    # pdb.set_trace()
    
    # 向上滑动一个屏幕的高度
    # swipe((screenWidth * 0.5, screenHeight * 0.9), vector=[0, -0.8], duration=2.5)
    # swipe(Template(r"tpl1681483473653.png", record_pos=(0.017, 0.216), resolution=(750, 1334)), vector=[-0.0286, -0.4442])


    # 等滚动动画结束
    sleep(3)

