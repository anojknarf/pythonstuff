from pyprocessing import *
import serial
threshold = 512
spread=1
height=480
width=640
values=[0 for xx in range(width)]
values2=[0 for xx in range(width)]
port = serial.Serial('COM11', 9600)

def setup():
    size(640, 480)
    smooth()

def serialed():
    myString = port.readline().strip('\r\n').strip()
    global val
    global val2
    try:
        print(myString)
        (val,val2, _) = myString.split(',')    
        val=float(val)
        val2=float(val2)
    except:
        serialed()
        
def getY(valu):
    return(((valu / 1023.0) * height) - 1)

def draw():
    for i in range(0,width-1):
            values[i]= values[i+1]
            values2[i]= values2[i+1]
    serialed()
    values[width-1] = val
    values2[width-1] = val2
    strokeWeight(1)
    scale(spread,1)
    background(255)
    stroke(255)
    textSize(25)
    textAlign(LEFT)
    scale((1/spread),1)
    fill(180,0,0)
    text("Ver = " + str(val * 5/1024) + "V", width-250,70)
    fill(0,180,0)
    text("Hor = " + str(val2 * 5/1024) + "V", width-250,35)
    for x in range(1,width):
        stroke(180,0,0)
        line(width-x, height-1-getY(values[x-1]),width-1-x, height-1-getY(values[x]))
        stroke(0,180,0)
        line(width-x, height-1-getY(values2[x-1]),width-1-x, height-1-getY(values2[x]))
    port.flushInput()

run()
port.close()

