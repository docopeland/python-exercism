from math import sqrt, ceil, floor

def cipher_text(plain_text):
    text = "".join([val for val in plain_text.lower() if val.isalnum()])
    c = ceil(sqrt(len(text)))
    r = round(sqrt(len(text)))
    l = ["" for i in range(c)]
    for i in range(r):
        for j in range(c):
            try:
                l[j] = l[j] + text[i*c + j]
            except IndexError:
                l[j] = l[j] + " "
    for i in range(len(l)):
        if len(l)>0 and i+1 < len(l):
            l[i] = l[i] + " "
    return "".join(l)
