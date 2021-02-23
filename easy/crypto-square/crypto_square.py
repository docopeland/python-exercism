from math import sqrt, pow

def cipher_text(plain_text):
    text = [val for val in plain_text if val.isalnum()]
    if sqrt(len(text)) % 1 == 0:
        num = len(text)
    else:
        for val in range(len(text),len(text)*2):
            if sqrt(val) % 1 == 0:
                num = val
                break
    