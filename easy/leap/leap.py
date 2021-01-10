def leap_year(year):
    return year % 400 == 0 or (year % 4 ==0 and year % 100 != 0)
# either it's divisible by 400 or (multiple of 4 and not 100)