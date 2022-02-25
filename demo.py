import subprocess
import os
import sys
from urllib.request import urlopen
from json import load
from random import choice
from time import sleep


def tracert(a='', h=50, w=30):
    tArgs = ["tracert", "-h", str(h), "-w", str(w), "-d", str(a)]
    if a:
        subprocess.run(tArgs)

def where(address=''):
    def fix(a=''):
        if a:
            return 'https://ipinfo.io/' + a + '/json'
        else:
            return 'https://ipinfo.io/json'

    try:
        res = urlopen(fix(address))
    except:
        print("Bad address.")
        return

    data = load(res)
    #will load the json response into data

    for attr in data.keys():
        #will print the data line by line
        print(attr,' '*13+'\t->\t',data[attr])

def colorShift():
    def hexColor():
        return str(hex(choice(range(16))))[2:]

    _=os.system("color 0" + hexColor())

loading = [
r".____                            .___ .__                    ",
r"|    |       ____   _____      __| _/ |__|   ____      ____  ",
r"|    |      /  _ \  \__  \    / __ |  |  |  /    \    / ___\ ",
r"|    |___  (  <_> )  / __ \_ / /_/ |  |  | |   |  \  / /_/  >",
r"|_______ \  \____/  (____  / \____ |  |__| |___|  /  \___  / ",
r"        \/               \/       \/            \/  /_____/  "
]

def loading():
    width = os.get_terminal_size()[0]
    frameSize = width // 20
    alignments = ['^', '<', '>']

    def getWeirdChar():
        chars = ['\xa1', '\xa2', '\xa3', '\xa4', '\xa5',
        '\xa6', '\xa7', '\xa8', '\xa9', '\xac']
        return choice(chars)

    def renderRow(length, align):
        print('{:{a}{w}}'.format(length * getWeirdChar(), w=width, a=align), end="")
        sys.stdout.flush()

    try:
        i = 0
        growing = True
        align = '^'

        while(True):
            renderRow(i, align)
            sleep(.03)
            a = not ((i>1) or growing)
            b = not((i<width) or not growing)

            if i < width and growing:
                i += frameSize
            elif a or b:
                growing = not growing
                align = choice(alignments)
                for _ in loading:
                    sleep(.2)
                    print("{:{a}{w}}".format(_, a=align, w=width), end="")
                    sys.stdout.flush()
                    colorShift()
                sleep(.5)
            else:
                i -= frameSize
    except:
        os.system("color 0a")
