import random
import string
import math

class Cipher:
    def __init__(self, key=None):
        self.abc = "abcdefghijklmnopqrstuvwxyz"
        if key is None:
            self.key = ''.join(random.choices(string.ascii_lowercase, k = 100)) if not key else key
        else:
            self.key = key

    def cipher(self, text, keyno):
        cipher = self.abc[keyno:] + self.abc[:keyno]
        trans = str.maketrans(self.abc,cipher)
        return str.translate(text,trans)

    def keylen(self, text):
        if len(self.key) < len(text):
            return self.key * (math.ceil(len(text)/len(self.key)))
        else:
            return self.key

    def encode(self, text):
        key = self.keylen(text)
        return "".join([self.cipher(text[i],self.abc.index(key[i])) for i in range(len(text))])

    def decode(self, text):
        key = self.keylen(text)
        return "".join([self.cipher(text[i],26-self.abc.index(key[i])) for i in range(len(text))])
