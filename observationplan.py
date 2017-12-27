from __future__ import print_function
import sched, time
import xml.etree.ElementTree as ET
import time
import datetime

import rts2.rtsapi


j=rts2.rtsapi.createProxy(url='http://localhost:8889', username='ismail',password='ismail')



def move_telescope(alt, az):
    print('alt is ', str(alt), ' az is ', str(az))
    command = 'altaz ' + str(alt) + ' ' + str(az)
    j.executeCommand('T0', command)


def expose(exposureTime, exposureNumber):
    print('exposure time  is ', str(exposureTime), ' exposure number ', str(exposureNumber))
    print (time.time())
    command = 'fast ' + str(exposureTime) + ' ' + str(exposureNumber)
    #j.executeCommand('C0', command)

def timeToUnixTimeStamp(dateString):

    date, times, fraction = dateString.split('_');

    datePlusTime = date + times

    unixTimeStamp = time.mktime(datetime.datetime.strptime(datePlusTime, "%Y%m%d%H%M%S").timetuple())


    unixTimeStampString = str(unixTimeStamp)
    unixTime, fract = unixTimeStampString.split('.')
    unixTimeStampString = unixTime + '.' + fraction

    return unixTimeStampString


tree = ET.parse('/home/ismail/test.xml')

root=tree.getroot()


# The dot represents current nested level from root, else you must include other parent tags here
exposureStarts = []
for node in root.findall("./observationPlan/Slots/Lines/ImageLine/Time"):
    # tag.text is the attribute for the text between the tag
    exposureStarts.append(node.text)
   # print node.text

exposureTimes = []
for node in root.findall("./observationPlan/Slots/Lines/ImageLine/ExposureTime"):
    exposureTimes.append(node.text)
    #print node.text

exposureNumbers=[]
for node in root.findall("./observationPlan/Slots/Lines/ImageLine/FrameNumber"):
    exposureNumbers.append(node.text)
    #print node.text


mountStarts = []
for node in root.findall("./observationPlan/Slots/Lines/MountLine/Time"):
    # tag.text is the attribute for the text between the tag
    mountStarts.append(node.text)
   # print node.text

mountAzimuths = []
for node in root.findall("./observationPlan/Slots/Lines/MountLine/Azimuth"):
    mountAzimuths.append(node.text)
    #print node.text

mountAltitudes=[]
for node in root.findall("./observationPlan/Slots/Lines/MountLine/Elevation"):
    mountAltitudes.append(node.text)
    #print node.text



'''
for lineID,exposureStart in enumerate(exposureStarts):

   print ('exposure Start time ' , exposureStart, ' startTime To unixtime stamp ',
          timeToUnixTimeStamp(exposureStart),' exposure time ' , exposureTimes[lineID],
          ' number of exposures ', exposureNumbers[lineID],
          ' mount start time ' , mountStarts[lineID],
          ' goto azimuth ' , mountAzimuths[lineID],
          ' go to altitude ' ,mountAltitudes[lineID])

'''


mountSchedule = sched.scheduler(time.time, time.sleep)
now = time.time()
print('now is ', now)
events = []
i=0
for lineID,exposureStart in enumerate(exposureStarts):
    print ('i is ', i)
    mountSchedule.enterabs(float(timeToUnixTimeStamp(mountStarts[lineID])),1,move_telescope,(mountAltitudes[lineID],mountAzimuths[lineID],))
    i=i+1




cameraSchedule =sched.scheduler(time.time, time.sleep)


for lineID,mountStart in enumerate(mountStarts):
    print ('i is ', i)
    cameraSchedule.enterabs(float(timeToUnixTimeStamp(exposureStarts[lineID])),1,expose,(exposureTimes[lineID],exposureNumbers[lineID],))
    i=i+1


mountSchedule.run()
cameraSchedule.run()