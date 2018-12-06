import bsmLib.RPL as RPL
from vec_angle import vec_angle 
from bsmLib.vector import vector
import time
from math import pi

f = open('gData.txt', 'r')
c = f.read()
f.close()

start = c.find("44")
end = c.find("',", start)
lat = c[start:end]
print lat

start2 = c.find("09")
end2 = c.find("')", start)
long = c[start2:end2]
print long
RPL.init() 

motorL = 0
motorR = 1
#2000 for right 1000 for left
Numberx1 = int(raw_input("x1 > "))
Numbery1 = int(raw_input("y1 > "))
Numberx2 = int(raw_input("x2 > "))
Numbery2 = int(raw_input("y2 > "))

def vec_trans_angle(x):
	TurnTime = abs(x) / 20
	#vectors are read in distances of 15.24 cm per unit
	if x > 0:
		move = time.time()
		#turns left
 		while time.time() < (move + TurnTime):
	  		RPL.servoWrite(motorL, 0)
			RPL.servoWrite(motorR, 2000)
		if time.time() > (move + TurnTime):
    			RPL.servoWrite(motorL, 0)
    			RPL.servoWrite(motorR, 0)
			
	
	if x < 0: 
		move2 = time.time()
		#turns right
		while time.time() < (move2 + TurnTime):
	  		RPL.servoWrite(motorL, 1000)
			RPL.servoWrite(motorR, 0)
		if time.time() > (move2 + TurnTime):
    			RPL.servoWrite(motorL, 0)
    			RPL.servoWrite(motorR, 0)
			

def vec_length(x1,y1):
  	v = vector(x1, y1) 
  	length = v.mag()
  	return length

def vec_trans_length(magnitude):
  #robot goes 13.3 cm in 1 second
  	Length = abs(magnitude) * 15.24
  	Runtime = Length / 12.3
  	move3 = time.time()
 	while time.time() < (move3 + Runtime):
    		RPL.servoWrite(motorL, 2000)
		RPL.servoWrite(motorR, 1000)
  	if time.time() > (move3 + Runtime):
    		RPL.servoWrite(motorL, 0)
    		RPL.servoWrite(motorR, 0)
		
	
def vec_combined(x1,y1,x2,y2):
	vec_trans_angle(vec_angle(x1,y1,x2,y2))
	vec_trans_length(vec_length(x2,y2))
	
vec_combined(Numberx1, Numbery1, Numberx2, Numbery2)
