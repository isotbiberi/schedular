import time
import datetime
from decimal import Decimal
dateString ='20160801_013736_747289331'
print dateString

date,times,fraction = dateString.split('_');
print 'date is ' , date , 'time is ', times ,'fraction is ', fraction
datePlusTime = date+times
print datePlusTime
unixTimeStamp =time.mktime(datetime.datetime.strptime(datePlusTime, "%Y%m%d%H%M%S").timetuple())
print unixTimeStamp

unixTimeStampString = str(unixTimeStamp)
unixTime,fract = unixTimeStampString.split('.')
unixTimeStampString = unixTime+ '.' + fraction

print unixTimeStampString