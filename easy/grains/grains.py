def square(number):
    if 1 <= number <= 64:
        return 2**(number-1)
    else:
        raise ValueError("number must be between 1 and 64")

def total():
    return sum([2**val for val in range(0,64)])
