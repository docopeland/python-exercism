def rotate(text:str, key:int):
    abc = "abcdefghijklmnopqrstuvwxyz"
    cipher = abc[key:] + abc[:key]
    trans = str.maketrans(abc + abc.upper(),cipher + cipher.upper())
    return str.translate(text,trans)
