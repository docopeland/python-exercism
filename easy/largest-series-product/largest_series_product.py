from math import prod

def largest_product(series, size):
    if size > len(series) or size < 0:
        raise ValueError("Size out of range")
    nums = [int(x) for x in series]
    return max(prod(nums[i:i+size]) for i in range(0,len(series)-size+1))