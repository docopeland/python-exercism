def is_armstrong_number(number):
    pow = len(str(number))
    if sum(map(lambda x: int(x)**pow,str(number))) == number:
        return True
    else:
        return False