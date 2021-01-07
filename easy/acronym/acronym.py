import re;

def abbreviate(words):
    return "".join(word for word in re.findall("(?<![A-Z'])[A-Z?]",words.upper()))
