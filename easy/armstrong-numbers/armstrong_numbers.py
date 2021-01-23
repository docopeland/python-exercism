def is_armstrong_number(number):
    num = str(number)
    sum = 0
    for val in num:
        sum = sum + int(val) ** len(num)
    if sum == number:
        return True
    else:
        return False