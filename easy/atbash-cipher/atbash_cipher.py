cipher = str.maketrans("abcdefghijklmnopqrstuvwxyz","zyxwvutsrqponmlkjihgfedcba")

def encode(plain_text: str):
    text = "".join([letter for letter in plain_text if letter.isalnum()])
    return spacing("".join([letter.translate(cipher) for letter in text.lower() if letter.isalnum()]))

def spacing(text:str):
    if len(text) < 6:
        return text
    else:
        return text[:5] + " " + spacing(text[5:])

def decode(ciphered_text):
    return "".join([letter.translate(cipher) for letter in ciphered_text.lower() if letter.isalnum()])
