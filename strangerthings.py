import sys
import time
import random
from neopixel import *

LED_COUNT   = 50
LED_PIN     = 18
LED_FREQ_HZ = 800000
LED_DMA     = 5
LED_BRIGHTNESS = 255
LED_INVERT  = False

letterToLight =[("a",0),("b",1),("c",2),("d",3),("e",4),("f",5),("g",6),("h",7),("i",8),("j",9),("k",10),("l",11),
                ("m",12),("n",13),("o",14),("p",15),("q",16),("r",17),("s",18),("t",19),("u",20),("v",21),("w",22),("x",23),
                ("y",24),("z",25),(" ",26)]
letterToLight = dict(letterToLight)

def animate(strip, color, wait_ms=50):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

    numOfLights = strip.numPixels() - 1
    for i in range(numOfLights, -1, -1):
        strip.setPixelColor(i, Color(0,0,0))
        strip.show()
        time.sleep(wait_ms/1000.0)

def randColor():
    rNum = random.randint(1,7)
    if rNum == 1:
        return Color(255,0,0)
    elif rNum == 2:
        return Color(0,255,0)
    elif rNum == 3:
        return Color(0,0,255)
    elif rNum == 4:
        return Color(127,127,0)
    elif rNum == 5:
        return Color(127,0,127)
    elif rNum == 6:
        return Color(0,127,127)
    else:
        return Color(255,255,255)

def turnPixelOn(strip, pos, timer = 2):
    strip.setPixelColor(pos, randColor())
    strip.show()
    time.sleep(timer/1)
    strip.setPixelColor(pos, Color(0,0,0))
    strip.show()
    time.sleep(timer)

def charIsSpace(timer = 3):
    strip.show()
    time.sleep(timer/2)

def userInput():
    while True:
        fromUpsideDown = raw_input("What do you want to say from the upsidedown??? ")
        if all(x.isalpha() or x.isspace() for x in fromUpsideDown):
            fromUpsideDown = fromUpsideDown.lower()
            with open("string.txt", "a") as f:
                f.write(fromUpsideDown + "\n")
            return fromUpsideDown
        else:
            print "you can only send letters from the upsidedown!"

def presetString():
    with open("string.txt") as f:
        for line in f:
            print line
            lightSelect(line.strip())

def lightSelect(fromUpsideDown):
    for x in range(0, len(fromUpsideDown)):
        letter = fromUpsideDown[x]
        light = letterToLight[letter]
        if light == 26:
            charIsSpace()
        else:
            turnPixelOn(strip, light)
    animate(strip, randColor())

if __name__ == '__main__':
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)

    if sys.argv[1] == "user":
        while True:
            strip.begin()
            strip.show()
            lightSelect(userInput())
    else:
        while True:
            strip.begin()
            strip.show()
            presetString()
