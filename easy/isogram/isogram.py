def is_isogram(string):
    listicle=[]
    listicle[:0] = string.lower()
    if " " in listicle: listicle.remove(" ")
    if "-" in listicle: listicle.remove("-")
    bool = True
    for letter in listicle:
        if listicle.count(letter) > 1: return False
        else: continue
    return bool