import re

def answer(question):
    nums = [int(i) for i in re.findall(r"[-]*[0-9]+",question)]
    opers = [re.findall(mod,question) for mod in ["plus","minus","multiplied","divided","cubed"] if re.findall(mod,question)]
    ops = [j for i in opers for j in i]
    if len(nums) < 1 or len(nums) != len(ops) +1:
        raise ValueError("need numbers")
    val = nums[0]
    for i in range(1,len(nums)):
        if ops[i-1] == "plus":
            val = val + nums[i]
        if ops[i-1] == "minus":
            val = val - nums[i]
        if ops[i-1] == "multiplied":
            val = val * nums[i]
        if ops[i-1] == "divided":
            val = val / nums[i]
    return val
