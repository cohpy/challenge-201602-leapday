import datetime

def nextLeapDayMeeting(lastYear):
    '''
    Finds the next date where the last Monday of February is also leap day.
    lastYear is the year of the last meeting. lastYear must be a valid leap year,
    meaning that it is a multiple of 4 while not being a multiple of 100 unless
    it is also a multiple of 400.
    '''
    
    if not (lastYear % 4 == 0 and (lastYear % 100 != 0 or lastYear % 400 == 0)):
        raise Exception('Not a valid leap year')
    
    leapDay = datetime.datetime.strptime("2/29/" + str(lastYear), "%m/%d/%Y")
    
    while True:
        # Add exactly 4 years +1 for leap day.
        # The result will be a monday if the year is not a multiple of 100
        leapDay = leapDay + datetime.timedelta(days=1461)
        
        if leapDay.day == 1: # If the leapday is cancelled
            leapDay = leapDay + datetime.timedelta(days=1460) # Add 4 years
            continue

        if leapDay.weekday() == 0: # If it's a monday
            return leapDay # Then that's our answer, return it

answer = nextLeapDayMeeting(2016)
print answer.strftime("%m/%d/%Y")
