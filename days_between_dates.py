# Define a daysBetweenDates procedure that would produce the
# correct output if there was a correct nextDay procedure.
#
# Note that this will NOT produce correct outputs yet, since
# our nextDay procedure assumes all months have 30 days
# (hence a year is 360 days, instead of 365).
# 

def daysInMonth(month, year):
    """ Stub. Always returns 30 for now"""
    if isLeapYear(year):
        days = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    else:
        days = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    return days[month]

def isLeapYear(year):
    """ Stub returns False always 
    Leap year if divisible by 4, but not by 100.
    If divisible by 4 and 100 it must not be divisible by 400. """
    leapYear = False
    if (year % 4 == 0) and ((year %400 == 0) or (year %100 != 0)):
        leapYear = True
    
    return leapYear

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    # if (month in {1,3,5,7,8,10,12} and day < 31) or (month in {4,6,9,11} and day < 30) or  (month == 2 and day <28):
    #         return year, month, day + 1
    if day < daysInMonth(month, year):
        return year, month, day +1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1
 
def dateIsBefore(year1,month1,day1,year2,month2,day2):
    """Returns True if year1-month1-day1 is before
    year2-month2-day2. Otherwise, returns False """

    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2

    return False

       
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
        
    # YOUR CODE HERE!
    assert not dateIsBefore(year2,month2,day2,year1,month1,day1)
    days = 0
    while dateIsBefore(year1,month1,day1,year2,month2,day2):
        year1,month1,day1 = nextDay(year1,month1,day1)
        days = days + 1
    
    return days

def test():
    # test_cases = [((2013,5,5,2012,5,5),"AssertionError"),
    #               ((2012,1,1,2012,2,28),58),
    #               ((2012,9,30,2012,10,30),30), 
    #               ((2012,1,1,2013,1,1),360),
    #               ((2012,9,1,2012,9,4),3),
    #               ((2012,1,1,2012,3,1), 60),
    #               ((2011,6,30,2012,6,30), 366),
    #               ((2011,1,1,2012,8,8), 585 ),
    #               ((1900,1,1,1999,12,31), 36523)]

    # tests include leap year
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]

#  tests assume all months have 30 days, no leap years
    # test_cases = [((2012,9,30,2012,10,30),30), 
    #               ((2012,1,1,2013,1,1),360),
    #               ((2012,9,1,2012,9,4),3),
    #               ((2012,1,1,2012,1,1),0),
    #               ((2013,1,1,1999,12,31), "AssertionError")]
    
    for (args, answer) in test_cases:
        try:
            result = daysBetweenDates(*args)
            if result != answer:
                print "Test with data:", args, "failed"
            else:
                print "Test case passed!"
        except AssertionError:
            if answer == "AssertionError":
                print "Nice job! Test case {0} correctrly raised AssertionError \n".format(args)
            else:
                print "Check your work! Test case {0} should not raise AssertionError!".format(args)

if __name__ == '__main__':
    test()
    
