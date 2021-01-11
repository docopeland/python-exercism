import re

def is_pangram(sentence):
    abcs = "abcdefghijklmnopqrstuvwxyz"
    return len(set(re.findall("[a-z]",sentence.lower()))) >= 26