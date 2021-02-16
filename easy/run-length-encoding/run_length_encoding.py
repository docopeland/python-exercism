import re

def decode(string):
    return re.sub(r"(\d+)(\D)",lambda x: x.group(2) * int(x.group(1)),string)

def encode(string):
    return re.sub(r"(.)\1+",lambda x: str(len(x.group(0))) + x.group(1),string)