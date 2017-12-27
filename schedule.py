from __future__ import print_function
import sched, time
from datetime import datetime


import rts2.rtsapi


j=rts2.rtsapi.createProxy(url='http://localhost:8889', username='ismail',password='ismail')




def move_telescope(alt,az):
     print ('alt is ',str(alt) , ' az is ',str(az))
     command = 'altaz ' + str(alt) + ' ' + str(az)
     j.executeCommand('T0',command)



#get_image()


s = sched.scheduler(time.time, time.sleep)



now = time.time()
event1 = s.enterabs(now+1,1,move_telescope,(30,270,))
event2 = s.enterabs(now+2,1,move_telescope,(35,270,))
event3 = s.enterabs(now+3,1,move_telescope,(40,270,))
event4 = s.enterabs(now+4,1,move_telescope,(45,270))
event5 = s.enterabs(now+5,1,move_telescope,(50,270))
'''
event6 = s.enterabs(now+6,1,move_telescope,(60,60))
event7 = s.enterabs(now+7,1,move_telescope,(70,70))
event8 = s.enterabs(now+8,1,move_telescope,(80,80))
event9 = s.enterabs(now+9,1,move_telescope,(90,90))
event10 = s.enterabs(now+10,1,move_telescope,(100,100))
'''
s.run()