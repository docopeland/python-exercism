from datetime import date
from calendar import monthrange

def meetup(year:int, month:int, week, day_of_week):
    weeks = {"teenth":range(13,20),"1st":range(1,8),"2nd":range(8,15),"3rd":range(15,22),"4th":range(22,29),
             "5th":range(29,32),"last":range(31,20,-1)}
    weekday = {"Monday":0,"Tuesday":1,"Wednesday":2,"Thursday":3,"Friday":4,"Saturday":5,"Sunday":6}
    dt = [date(year, month, day) for day in weeks.get(week) if monthrange(year,month)[1] >= day and
          date(year, month, day).weekday() == weekday.get(day_of_week)]
    if len(dt) > 0:
        return dt[0]
    else:
        raise MeetupDayException("this does not exist")

class MeetupDayException(Exception):
    pass