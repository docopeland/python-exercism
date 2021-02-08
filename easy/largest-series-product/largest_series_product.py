def largest_product(series, size):
    if size > len(series) or size < 0:
        raise ValueError("Size out of range")
    else:
        val = None
        for i in range(len(series)-size+1):
            temp = 1
            for num in series[i:i+size]:
                temp = temp * int(num)
            if val is None or temp > val:
                val = temp
        return val