def rotate(text:str, key:int):
    abc = "abcdefghijklmnopqrstuvwxyz"
    cipher = abc[key:] + abc[:key]
    trans = str.maketrans(abc,cipher)
    return "".join([letter.translate(trans) for letter in text if letter.isalpha()])
