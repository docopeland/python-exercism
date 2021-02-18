alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
cipher = ["z","y","x","w","v","u","t","s","r","q","p","o","n","m","l","k","j","i","h","g","f","e","d","c","b","a"]

def encode(plain_text):
    text = ""
    for letter in plain_text.lower():
        if letter in alpha:
            abc = alpha.index(letter)
            text = text + cipher[abc]
        elif letter.isdigit():
            text = text + letter
        else:
            continue
    for num in range(len(text)-1,-1,-1):
        if num % 5 == 0 and num != 0:
            text = text[:num] + " " + text[num:]
    return text

def decode(ciphered_text):
    text = ""
    for letter in ciphered_text.lower():
        if letter in alpha:
            text = text + alpha[cipher.index(letter)]
        elif letter.isdigit():
            text = text + letter
        else:
            continue
    return text
