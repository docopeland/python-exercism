def steps(number,step=0):
    if number < 1:
        raise ValueError("Integer out of Range")
    elif int(number) == 1:
        return step
    else:
        return steps(number/2,step+1) if number % 2 == 0 else steps(3*number+1,step+1)

