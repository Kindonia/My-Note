#coding=utf8
from ctypes import Structure, windll, c_uint, sizeof, byref
import threading
import time
from pymouse import PyMouse

TIMEOUT = 30*5

class LASTINPUTINFO(Structure):
    _fields_ = [
        ('cbSize', c_uint),
        ('dwTime', c_uint),
    ]


def move():
    m = PyMouse()
    x, y = m.position()
    m.move(1919,1079)
    m.click(1919,1079)
    time.sleep(2)
    m.click(1919,1079)


def get_idle_duration():
    lastInputInfo = LASTINPUTINFO()
    lastInputInfo.cbSize = sizeof(lastInputInfo)
    windll.user32.GetLastInputInfo(byref(lastInputInfo))
    millis = windll.kernel32.GetTickCount() - lastInputInfo.dwTime
    return millis / 1000.0


def work():
    event = threading.Event()
    while not event.wait(20):
        s = get_idle_duration()
        print('Leave Time: {}s'.format(s))
        if s > TIMEOUT:
            move()

work()