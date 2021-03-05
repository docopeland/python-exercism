def classify(number):
    if number < 1:
        raise ValueError("number must be greater than 0")
    tots = sum([num for num in range(1,number) if number%num == 0])
    if tots > number:
        return "abundant"
    elif tots < number:
        return "deficient"
    else:
        return "perfect"

