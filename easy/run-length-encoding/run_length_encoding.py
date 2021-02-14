import re

def decode(string):
    dec = ""
    decString = string
    while len(decString) > 0:
        if re.match("[0-9]+",decString):
            num = int(re.match("[0-9*]+",decString).group()) - 1
            start = re.match("[0-9*]+",decString).span()[1]
            dec = dec + num*decString[start]
            decString = decString[start:]
        else:
            dec = dec + decString[0]
            decString = decString[1:]
    return dec

def encode(string):
    enc = ""
    count = 1
    for i in range(len(string)):
        if i + 1 < len(string):
            if string[i] == string[i+1]:
                count = count + 1
                continue
            else:
                if count == 1:
                    enc = enc + string[i]
                else:
                    enc = enc + str(count) + string[i]
                    count = 1
        else:
            if count == 1:
                enc = enc + string[i]
            else:
                enc = enc + str(count) + string[i]
    return enc
