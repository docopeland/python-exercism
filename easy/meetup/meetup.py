from datetime import date


def meetup(year:int, month:int, week, day_of_week):
    weeks = {"teenth":range(13,20),"1st":range(1,8),"2nd":range(8,15),"3rd":range(15,22),"4th":range(22,29),
             "5th":range(29,32),"last":(21,32)}
    weekday = {"Monday":0,"Tuesday":1,"Wednesday":2,"Thursday":3,"Friday":4,"Saturday":5,"Sunday":6}
    if week in weeks:
        days = weeks.get(week)
        for day in days:
            print(year,month,day,day_of_week,date(year, month, day).weekday())
            if date(year, month, day).weekday() == weekday.get(day_of_week):
                return date(year, month, day)

def MeetupDayException():
    raise MeetupDayException()