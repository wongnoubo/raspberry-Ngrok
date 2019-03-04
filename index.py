#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import get,post,run,request,template
import RPi.GPIO as GPIO
import time
#phy 29 31 37
def controlLed(cmd):
    controller ={
        "空调开" : 1,
        "卧室灯开" : 2,
        "排气扇开" : 3,
        "冰箱开" : 4,
        "电饭煲开" : 5,
        "加湿器开" : 6,
        "窗帘开" : 7,
        "空调关": 8,
        "卧室灯关": 9,
        "排气扇关": 10,
        "冰箱关": 11,
        "电饭煲关": 12,
        "加湿器关": 13,
        "窗帘关": 14,
    }
    return controller[cmd]

def controlIo(id):
    GPIO.setmode(GPIO.BCM)
    time.sleep(1)
    GPIO.setup(5, GPIO.OUT)
    GPIO.output(5, GPIO.LOW)
    GPIO.setup(6, GPIO.OUT)
    GPIO.output(6, GPIO.LOW)
    GPIO.setup(26, GPIO.OUT)
    GPIO.output(26, GPIO.LOW)
    time.sleep(0.02)
    if id == 1:
        GPIO.output(26, GPIO.LOW)
        GPIO.output(5, GPIO.LOW)
        GPIO.output(6, GPIO.HIGH)
    elif id == 2:
        GPIO.output(26, GPIO.LOW)
        GPIO.output(5, GPIO.HIGH)
        GPIO.output(6, GPIO.LOW)
    elif id == 3:
        GPIO.output(26, GPIO.LOW)
        GPIO.output(5, GPIO.HIGH)
        GPIO.output(6, GPIO.HIGH)
    elif id == 4:
        GPIO.output(26, GPIO.HIGH)
        GPIO.output(5, GPIO.LOW)
        GPIO.output(6, GPIO.LOW)
    elif id == 5:
        GPIO.output(26, GPIO.HIGH)
        GPIO.output(5, GPIO.LOW)
        GPIO.output(6, GPIO.HIGH)
    elif id == 6:
        GPIO.output(26, GPIO.HIGH)
        GPIO.output(5, GPIO.HIGH)
        GPIO.output(6, GPIO.LOW)
    elif id == 7:
        GPIO.output(26, GPIO.HIGH)
        GPIO.output(5, GPIO.HIGH)
        GPIO.output(6, GPIO.HIGH)
    else:
        GPIO.output(26, GPIO.LOW)
        GPIO.output(5, GPIO.LOW)
        GPIO.output(6, GPIO.LOW)

@get("/")
def index():
    return template("index")
@post("/cmd")
def cmd():
    print("按下了按钮: "+request.body.read().decode())
    id =controlLed(request.body.read().decode())
    print("id:"+str(id))
    controlIo(id)
    return "OK"
run(host="0.0.0.0")