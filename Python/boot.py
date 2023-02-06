import machine, neopixel


import time
import urandom
import copy

length = 50
np = neopixel.NeoPixel(machine.Pin(4), length + 1)

blinkyBugStatus = {
    'ticksUntilAction': 0,
    'nextActionType': 0, # 0 = normal, 1 = snappy
    'currentAction': 0,
    'actionTickstate': 20, # "count down" for the current action
    'pulseStreachTicks': 0, # add some variance for the 0.2 - 0.3ish range
    'colorRed': 0,
    'colorGreen': 0,
    'colorBlue': 0
    }
 
BLINKY_BUGS = []

animations = [[10,20,25,50,75,120,120,150,200,255,255,200,150,100,50,40,30,20,20,40],
              [10,10,20,20,25,25,50,50,75,75,120,120,150,150,200,200,255,255,150,100,50,40,30,20,20,30],
              [10,20,25,50,75,120,120,150,200,255,255,200,150,100,50,40,30,20,10,0,10,20,25,50,75,120,120,150,200,255,255,200,150,100,50,40,30,20,20,20],
              [20 ,200,30 ,190,40 ,180,50 ,170,60 ,160,70 ,150,80 ,140,90 ,130,100,120,110,110,120,100,130,90,140,80,150,70,160,60,170,50,180,40,190,30,200,100],
              [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200]]

def init_bugs():
    for i in range(length):
        BLINKY_BUGS.append(copy.copy(blinkyBugStatus))
        BLINKY_BUGS[i]['ticksUntilAction'] = BLINKY_BUGS[i]['actionTickstate'] + randint(10,100)
        BLINKY_BUGS[i]['currentAction'] = BLINKY_BUGS[i]['nextActionType']
        BLINKY_BUGS[i]['nextActionType'] = randint(0,len(animations)-1)
        BLINKY_BUGS[i]['actionTickstate'] = 20
        BLINKY_BUGS[i]['colorRed'] = 1
        BLINKY_BUGS[i]['colorGreen'] = 1
        BLINKY_BUGS[i]['colorBlue'] = 1


def do_tick():
    global FirstSeven
    for i in range(length):
        if (BLINKY_BUGS[i]['ticksUntilAction'] == 0): # reset ticks until next,
            BLINKY_BUGS[i]['ticksUntilAction'] = BLINKY_BUGS[i]['actionTickstate'] + randint(10,100)
            BLINKY_BUGS[i]['currentAction'] = BLINKY_BUGS[i]['nextActionType']
            BLINKY_BUGS[i]['nextActionType'] = randint(0,len(animations)-1)
            BLINKY_BUGS[i]['actionTickstate'] = 0
            BLINKY_BUGS[i]['colorRed'] = randint(0,100) / 100
            BLINKY_BUGS[i]['colorGreen'] = randint(0,100) / 100
            BLINKY_BUGS[i]['colorBlue'] = randint(0,100) / 100
        else:
            BLINKY_BUGS[i]['ticksUntilAction'] = BLINKY_BUGS[i]['ticksUntilAction'] - 1
            if (BLINKY_BUGS[i]['actionTickstate'] < len(animations[BLINKY_BUGS[i]['currentAction']])):
                intensity = animations[BLINKY_BUGS[i]['currentAction']][BLINKY_BUGS[i]['actionTickstate']]
                BLINKY_BUGS[i]['actionTickstate'] = BLINKY_BUGS[i]['actionTickstate'] + 1
                np[i] = (int(intensity * BLINKY_BUGS[i]['colorRed']), int(intensity * BLINKY_BUGS[i]['colorGreen']), int(intensity * BLINKY_BUGS[i]['colorBlue']))
    np.write()


def randint(min, max):
    span = max - min + 1
    div = 0x3fffffff // span
    offset = urandom.getrandbits(30) // div
    val = min + offset
    return val

def start_test():
    test = randint(1,11)
    if test == 1:
        test1()
    elif test == 2:
        test2()
    elif test == 3:
        test3()
    elif test == 4:
        test4()
    elif test == 5:
        test5()
    elif test == 6:
        test6()
    elif test == 7:
        test7()
    elif test == 8:
        test8()
    elif test == 9:
        test9()
    elif test == 10:
        test10()
    elif test == 11:
        test11()
    time.sleep(1)

def test1():
    for i in range(length):
        np[i] = (i*4,200-(i*4),0)
    np.write()
    
def test2():
    for i in range(length):
        np[i] = (200-(i*4),i*4,0)
    np.write()

def test3():
    for i in range(length):
        np[i] = (0,200-(i*4),i*4)
    np.write()

def test4():    
    for i in range(length):
        np[i] = (0,i*4,200-(i*4))
    np.write()

def test5():
    for i in range(length):
        np[i] = (200-(i*4),0,i*4)
    np.write()

def test6():
    for i in range(length):
        np[i] = (i*4,0,200-(i*4))
    np.write()

def test7():
    for i in range(length):
        np[i] = (255,0,0)
    np.write()

def test8():
    for i in range(length):
        np[i] = (0,255,0)
    np.write()

def test9():
    for i in range(length):
        np[i] = (0,0,255)
    np.write()
    time.sleep(1)
    for l in range(4):
        for t in range(20):
            for i in range(length/2):
                np[i] = (randint(0,255),randint(0,255),randint(0,255))
                np[i+25] = (0,0,0)
            np.write()
        for t in range(20):
            for i in range(0,25):#length/2):
                np[i+25] = (randint(0,255),randint(0,255),randint(0,255))
                np[i] = (0,0,0)
            np.write()
        for t in range(20):
            for i in range(0,50):#length/2):
                np[i] = (randint(0,255),randint(0,255),randint(0,255))
            np.write()

def test10():
    for i in range(length):
        np[i] = (255,255,255)
        np.write()
        
def test11():
    for tickcount in range(250):
        do_tick()
    time.sleep(.5)

def melt_away3():
    for l in range(3):
        for x in range(length):
            for i in range(length):
                if x == i:
                    np[i] = (255,255,255)
                elif i == (x-1):
                    if l == 0:
                        np[i] = (0,0,0)
                    elif l == 1:
                        np[i] = (0,randint(0,255),randint(0,255))
                    elif l == 2:
                        c = randint(0,255)
                        np[i] = (c,c,c)
            np.write()
            time.sleep(.01)
        for x in range(length):
            for i in range(length):
                if x == i:
                    np[50-i] = (255,255,255)
                elif i == (x-1):
                    if l == 0:
                        np[50-i] = (randint(0,255),randint(0,255),0)
                    elif l == 1:
                        np[50-i] = (randint(0,255),0,randint(0,255))
                    elif l == 2:
                        np[50-i] = (0,0,0)
            np.write()
            time.sleep(.01)
        
def melt_away4():
    for l in range(3):
        for i in range(0,50,5):
            for c in range(length):
                if c < i:
                    if l == 0:
                        np[c] = (0,0,0)
                    elif l == 1:
                        np[c] = (0,255,0)
                    elif l == 2:
                        np[c] = (255,255,255)
            np[i] = (255,255,255)
            np[i+1] = (255,255,255)
            np[i+2] = (255,255,255)
            np[i+3] = (255,255,255)
            np[i+4] = (255,255,255)
            np.write()
            time.sleep(.01)
        for i in range(45,-5,-5):
            for c in range(length):
                if c > i+4:
                    if l == 0:
                        np[c] = (255,0,0)
                    elif l == 1:
                        np[c] = (0,0,255)
                    elif l == 2:
                        np[c] = (0,0,000)
            np[i] = (255,255,255)
            np[i+1] = (255,255,255)
            np[i+2] = (255,255,255)
            np[i+3] = (255,255,255)
            np[i+4] = (255,255,255)
            np.write()
            time.sleep(.01)
    for i in range(length):
        np[i] = (0,0,0)
    np.write()


def try_clear(dots):
    dot = randint(0,49)
    if dots[dot] == 'Y':
        dots[dot] = 'N'
        np[dot] = (0,0,0)
        np.write()
        time.sleep(.02)
        return False
    else:
        return True
        
def melt_away2():
    for x in range(255,-10,-10):   
        for i in range(length):
            np[i] = (x,x,x)
        np.write()

def melt_away1():
    dots = []
    for i in range(50):
        dots.extend('Y')
    for i in range(50):
        while try_clear(dots):
            print(".")
    
def melt_away():
    melt = randint(1,4)
    if melt == 1:
        melt_away1()
    elif melt == 2:
        melt_away2()
    elif melt == 3:
        melt_away3()
    elif melt == 4:
        melt_away4()


init_bugs()
while 1 == 1:
    start_test()
    melt_away()

