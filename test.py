#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()

'''
#delay(2000)
#x=mouse_point()
x=724902


#fake_window(x)
y=get_pixel_color(x,11,24)
print('%x' % y)

t1,t2,t3,t4=get_client_rect(x)
intx,inty=find_picture(x,0,0,t3,t4,"图片.bmp",0.9)
print(intx,inty)
strs=get_window_title(x)
print(strs)

move_window(x,0,0)
strs=get_window_rect(x)
print(strs)
bring_window_2_top(x)



key_down(x,"SHIFT")
delay(200)
key_down(x,"A")
delay(200)
key_up(x,"A")
delay(200)
key_up(x,"SHIFT")
delay(200)

delay(3000)
print("end")
#restore_window(x)

key_down(x,"ENTER")
delay(200)
key_up(x,"ENTER")
'''


'''
dll2 = windll.LoadLibrary('xDll.dll')
print("ss")
dll2.LR_Delay(1000)
print("ss")
x=c_int()
x=dll2.LR_MousePoint()

y=dll2.LR_GetWindowTitle(x)
print (c_wchar_p(y).value)

dll2.LR_Delay(5000)


intx=c_int()
inty=c_int()
pintx=pointer(intx)
pinty=pointer(inty)

strs=c_wchar_p("y.bmp")
sim=c_float(0.9)

result=dll2.LR_FindPictrue(x,0,0,640,480,strs,sim,pintx,pinty)
print (result)
print (intx.value,inty.value)
#dll2.SetFakeWindow(x)

dll2.SetFakeWindow(x)
time.sleep(10)


intx=dll2.LR_GetPixelColor(x,112,27)
print (intx)

'''

