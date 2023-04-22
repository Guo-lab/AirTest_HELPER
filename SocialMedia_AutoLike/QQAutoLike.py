# -*- encoding=utf8 -*-
__author__ = "gsq"

from airtest.core.api import *
from poco.drivers.ios import iosPoco


auto_setup(__file__)
connect_device("ios:///127.0.0.1:8100")

poco = iosPoco()

from airtest.cli.parser import cli_setup
if not cli_setup():
    auto_setup(__file__, devices=["ios:///127.0.0.1:8100"], logdir=r"/Users/gsq/Desktop/AirTest_HELPER/SocialAutoLike/QQAutoLike")  
    
    
# home()
# poco("Window").offspring("Home screen icons").child("Other").child("Other").offspring("常用")[0].click() 
# touch(Template(r"tpl1682093684684.png", record_pos=(0.229, -0.271), resolution=(750, 1334)))
# wait(Template(r"tpl1682093816714.png", record_pos=(0.324, -0.781), resolution=(750, 1334)))
# # poco("Window").offspring("超级QQ秀").click()

# poco("动态").click()



# home()
# poco("Window").offspring("Home screen icons").child("Other").child("Other").offspring("常用")[0].click() 
# touch(Template(r"tpl1682093684684.png", record_pos=(0.229, -0.271), resolution=(750, 1334)))
# wait(Template(r"tpl1682093816714.png", record_pos=(0.324, -0.781), resolution=(750, 1334)))
# # poco("Window").offspring("超级QQ秀").click()
# poco("动态").click()




screenWidth, screenHeight = poco.get_screen_size()
print(screenWidth, " ", screenHeight)

x = 100
while x > 0:
    x -= 1
    
#     if exists(Template(r"tpl1682101681447.png", record_pos=(0.121, -0.179), resolution=(750, 1334))):
#         break

    likeList = poco("Table").offspring("赞")
    if len(likeList) == 0:
        print(len(likeList))
        swipe((screenWidth * 0.5, screenHeight * 0.9), vector=[0, -0.6], duration=0.5)
        sleep(1)
        continue
        
    for child in likeList:
        childX, childY = child.get_position()
        if (childY >= 0.1 and childY < 0.8):
            child.click()
#         if poco("详情").exists():
#             poco("详情").offspring("Button").click()
    
    swipe((screenWidth * 0.5, screenHeight * 0.9), vector=[0, -0.6], duration=0.5)
    sleep(1)


