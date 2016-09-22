#!/usr/bin/env python3
# -*- coding: utf-8 -*-
key_map={
    "LBUTTON":1,
    "RBUTTON":2,
    "CANCEL":3,
    "MBUTTON":4,
    "BACKSPACE":8,
    "TAB":9,
    "CLEAR":12,
    "ENTER":13,
    "SHIFT":16,
    "CTRL":17,
    "MENU":18,
    "PAUSE":19,
    "CAPSLOCK":20,
    "ESC":27,
    "SPACE":32,
    "PAGEUP":33,
    "PAGEDOWN":34,
    "END":35,
    "HOME":36,
    "LEFT":37,
    "UP":38,
    "RIGHT":39,
    "DOWN":40,
    "SELECT":41,
    "PRINTSCREEN":42,
    "EXECUTE":43,
    "SNAPSHOT":44,
    "INS":45,
    "DEL":46,
    "HELP":47,

    '0':48,
    "1":49,
    "2":50,
    "3":51,
    "4":52,
    "5":53,
    "6":54,
    "7":55,
    "8":56,
    "9":57,

    "A":65,
    "B":66,
    "C":67,
    "D":68,
    "E":69,
    "F":70,
    "G":71,
    "H":72,
    "I":73,
    "J":74,
    "K":75,
    "L":76,
    "M":77,
    "N":78,
    "O":79,
    "P":80,
    "Q":81,
    "R":82,
    "S":83,
    "T":84,
    "U":85,
    "V":86,
    "W":87,
    "X":88,
    "Y":89,
    "Z":90,

    "NUMPAD0":96,
    "NUMPAD1":97,
    "NUMPAD2":98,
    "NUMPAD3":99,
    "NUMPAD4":100,
    "NUMPAD5":101,
    "NUMPAD6":102,
    "NUMPAD7":103,
    "NUMPAD8":104,
    "NUMPAD9":105,
    "NUMPAD*":106,
    "NUMPAD+":107,
    "NUMPADENTER":108,
    "NUMPAD-":109,
    "NUMPAD.":110,
    "NUMPAD/":111,

    "F1":112,
    "F2":113,
    "F3":114,
    "F4":115,
    "F5":116,
    "F6":117,
    "F7":118,
    "F8":119,
    "F9":120,
    "F10":121,
    "F11":122,
    "F12":123,
    "F13":124,
    "F14":125,
    "F15":126,
    "F16":127,
}


from ctypes import *

dll = windll.LoadLibrary('xDll.dll')

'''窗口操作'''


def get_pixel_color(hwnd, x, y):
    int_hwnd = c_int(hwnd)
    int_x = c_int(x)
    int_y = c_int(y)
    color = dll.LR_GetPixelColor(int_hwnd, int_x, int_y)
    return color


def find_picture(hwnd, left, top, right, bottom, picName, similar):
    if isinstance(left, str):
        left = int(left)
    if isinstance(top, str):
        top = int(top)
    if isinstance(right, str):
        right = int(right)
    if isinstance(bottom, str):
        bottom = int(bottom)
    int_hwnd = c_int(hwnd)
    int_left = c_int(left)
    int_top = c_int(top)
    int_right = c_int(right)
    int_bottom = c_int(bottom)
    intx = c_int()
    inty = c_int()
    pintx = pointer(intx)
    pinty = pointer(inty)
    strs = c_wchar_p(picName)
    sim = c_float(similar)
    dll.LR_FindPictrue(int_hwnd, int_left, int_top, int_right, int_bottom, strs, sim, pintx, pinty)
    return intx.value, inty.value


def foreground():
    int_hwnd = dll.LR_Foreground()
    return int_hwnd


def mouse_point():
    int_hwnd = dll.LR_MousePoint()
    return int_hwnd


def find_window(strName):
    strs = c_wchar_p(strName)
    int_hwnd = dll.LR_FindWindow(strs)
    return int_hwnd


def get_window_rect(hwnd):
    int_hwnd = c_int(hwnd)
    strs = dll.LR_GetWindowRect(int_hwnd)
    a, b, c, d = c_wchar_p(strs).value.split("|")
    return int(a),int(b),int(c),int(d)


def get_client_rect(hwnd):
    int_hwnd = c_int(hwnd)
    strs = dll.LR_GetClientRect(int_hwnd)
    a,b,c,d =c_wchar_p(strs).value.split("|")
    return int(a),int(b),int(c),int(d)


def get_window_title(hwnd):
    int_hwnd = c_int(hwnd)
    strs = dll.LR_GetWindowTitle(int_hwnd)
    return c_wchar_p(strs).value


def set_window_title(hwnd, winName):
    int_hwnd = c_int(hwnd)
    strs = c_wchar_p(winName)
    dll.LR_SetWindowTitle(int_hwnd, strs)
    return


def move_window(hwnd, x, y):
    int_hwnd = c_int(hwnd)
    int_x = c_int(x)
    int_y = c_int(y)
    dll.LR_MoveWindow(int_hwnd, int_x, int_y)
    return


def bring_window_2_top(hwnd):
    int_hwnd = c_int(hwnd)
    dll.LR_WindowBring2Top(int_hwnd)
    return


'''鼠标操作'''


def key_down(hwnd, key):
    if isinstance(key,str):
        key=key_map[key]
    dll.LR_KeyDown(hwnd,key)
    return


def key_up(hwnd, key):
    if isinstance(key,str):
        key=key_map[key]
    dll.LR_KeyUp(hwnd, key)
    return


def left_down(hwnd):
    dll.LR_LeftDown(hwnd)
    return


def left_up(hwnd):
    dll.LR_LeftUp(hwnd)
    return


def right_down(hwnd):
    dll.LR_RightDown(hwnd)
    return


def right_up(hwnd):
    dll.LR_RightUp(hwnd)
    return


def middle_down(hwnd):
    dll.LR_MiddleDown(hwnd)
    return


def middle_up(hwnd):
    dll.LR_MiddleUp(hwnd)
    return


def mouse_move(hwnd):
    dll.LR_Move(hwnd)
    return


def delay(delay_time):
    dll.LR_Delay(delay_time)
    return


'''
hookwindow
'''

def fake_window(hwnd):
    dll.SetFakeWindow(hwnd)
    return


def restore_window(hwnd):
    dll.RestoreWindow(hwnd)
    return

