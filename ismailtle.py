#!/usr/bin/env python
from __future__ import print_function
import sched, time
from datetime import datetime


import rts2.rtsapi


j=rts2.rtsapi.createProxy(url='http://localhost:8889', username='ismail',password='ismail')

tle = 'move_tle "1 35932U 09051B   17339.93395837 +.00000152 +00000-0 +45393-4 0  9993" "2 35932 098.5188 121.7723 0008763 085.5782 274.6416 14.56095107435274"'
j.executeCommand('T0',tle)
#j.executeCommand('T0','altaz 50 70')
j.setValue('T0','TRACKING','off')
#j.executeCommand('C0','fast 1 1')




'''
def move_telescope(alt,az):
     print ('alt is ',str(alt) , ' az is ',str(az))
     command = 'altaz ' + str(alt) + ' ' + str(az)
     j.executeCommand('T0',command)



def fast_exposure(exptime,expcount):
    print ('exptime is ',exptime, ' expcount is ' , expcount)
    command = 'fast ' + str(exptime) + ' ' + str(expcount) 	
    j.executeCommand('C0',command)

s = sched.scheduler(time.time, time.sleep)



now = time.time()
event1 = s.enterabs(now+2,1,move_telescope,(25.09,160.74,)) #mountline 10 .013602_59
event2 = s.enterabs(now+4,1,fast_exposure,(0.025,40,)) #013606_48

event3 = s.enterabs(now+6,1,move_telescope,(26.4,160.36,))#013606_13
event4 = s.enterabs(now+8,1,fast_exposure,(0.025,40,)) #013610_57

event5 = s.enterabs(now+10,1,move_telescope,(27.77,159.94,))#013610_56
event6 = s.enterabs(now+12,1,fast_exposure,(0.025,40,))#013614_51

event7 = s.enterabs(now+13.5,1,move_telescope,(29.18,159.49,))#013613_83
event8 = s.enterabs(now+16,1,fast_exposure,(0.025,40,))#013618_30

event9 = s.enterabs(now+17.8,1,move_telescope,(30.66,159.01,))#013617_47
event10 = s.enterabs(now+19,1,fast_exposure,(0.025,40,))#013621_96
'''


'''
event6 = s.enterabs(now+6,1,move_telescope,(60,60))
event7 = s.enterabs(now+7,1,move_telescope,(70,70))
event8 = s.enterabs(now+8,1,move_telescope,(80,80))
event9 = s.enterabs(now+9,1,move_telescope,(90,90))
event10 = s.enterabs(now+10,1,move_telescope,(100,100))
'''
#s.run()
