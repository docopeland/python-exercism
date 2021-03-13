import re

def answer(question):
    nums = [int(i) for i in re.findall(r"[-]*[0-9]+",question)]
    ops = [re.findall(mod,question) for mod in ["plus","minus","multiplied","divided"] if re.findall(mod,question)]
    val = 0
    if len(nums) < 1 or len(nums) != len(ops) +1:
        raise ValueError("need numbers")
    for i in range(len(ops)):
        if ops[i] == ["plus"]:
            val = val + nums[i]+nums[i+1]
        if ops[i] == ["minus"]:
            val = val + nums[i]-nums[i+1]
        if ops[i] == ["multiplied"]:
            val = val + nums[i]*nums[i+1]
        if ops[i] == ["divided"]:
            val = val + nums[i]/nums[i+1]
    return val
    print(question,nums,ops[0],val)
