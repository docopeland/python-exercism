import re

def decode(string):
    dec = ""
    for i in range(len(string)):
        if re.match("[1-9]"):
            dec = dec + int(string[i])*string[i+1]
        else:
            continue
    return dec





def encode(string):
    dec = ""
    count = 1
    for i in range(1,len(string)):
        if string[i-1] == string[i]:
            count = count + 1
        else:
            if count == 1:
                dec = dec + string[i-1]
            else:    
                dec = dec + str(count)+string[i-1]
            count = 1
    return dec
