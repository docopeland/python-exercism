cipher = str.maketrans("abcdefghijklmnopqrstuvwxyz","zyxwvutsrqponmlkjihgfedcba")

def encode(plain_text: str):
    return spacing(nospacing(plain_text).translate(cipher))

def decode(ciphered_text):
    return nospacing(ciphered_text.translate(cipher))

def spacing(text:str):
    if len(text) < 6:
        return text
    else:
        return text[:5] + " " + spacing(text[5:])

def nospacing(text:str):
    return "".join([letter for letter in text.lower() if letter.isalnum()])