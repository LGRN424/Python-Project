import datetime
import time

from datetime import datetime, timedelta, tzinfo

print "Is the bank branch open?"
print
print 


class Zone(tzinfo):
    def __init__(self,offset,isdst,name):
        self.offset = offset
        self.isdst = isdst
        self.name = name
    def utcoffset(self, dt):
        return timedelta(hours=self.offset) + self.dst(dt)
    def dst(self, dt):
            return timedelta(hours=1) if self.isdst else timedelta(0)
    def tzname(self,dt):
         return self.name
        
PST = Zone(-8,False,'PST')
GMT = Zone(0,False,'GMT')
EST = Zone(-5,False,'EST')


time1 = datetime.utcnow().strftime('%H:%M')
time2 = datetime.now(EST).strftime('%H:%M')

print "Portland date and time:",datetime.now(PST).strftime('%m/%d/%Y %H:%M %Z')
print
print "The date and time in London:",datetime.now(GMT).strftime('%m/%d/%Y %H:%M %Z')
print
print ("The London branch is open from 09:00am until 09:00pm GMT")
print
print "The date and time in New York:",datetime.now(EST).strftime('%m/%d/%Y %H:%M %Z')
print
print ("The New York branch is open from 09:00am until 09:00pm EST")
print
if(time1 >= '09:00' and time1 < '21:00' and time2 >= '09:00' 
    and time2 < '21:00'):
        print "The London branch and New York branches are open"
elif (time1 < '09:00' or time1 >= '21:00' and time2 >= '09:00' 
    and time2 < '21:00'):
        print "Sorry, the London branch is closed but the New York branch is open"
elif(time1 >='09:00' and time1 < '21:00' and time2 < '09:00' or time2 >= '21:00'):
        print "The London branch is open but the New York branch is currently closed"
else:
        print "Sorry, both branches are closed"
    
print
print "Happy Banking!!"












