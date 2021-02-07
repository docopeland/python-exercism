import re

def translate(text: str):
    text = text.split()
    for i in range(len(text)):
        if re.search("^[aeiou].*",text[i]) or text[i].startswith("xr") or text[i].startswith("yt"):
            front = ""
        elif re.match(".*[qu]{2}",text[i]) is not None:
            front = (re.match(".*[qu]{2}",text[i])).group(0)
        elif re.match("[aeiou]",text[i]) is None:
            front = ""
            print(re.match("[y]",text[i]))
        else:
            front = (re.match("^[^aeiou]+",text[i])).group(0)
        text[i] = text[i][len(front):] + text[i][:len(front)] + "ay"
    return " ".join(text)
