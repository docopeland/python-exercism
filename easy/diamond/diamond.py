import string

def rows(letter):
    abc = enumerate(string.ascii_uppercase)
    indx = sum([key for key,val in abc if letter == val])*2-1
    val = []
    for let in string.ascii_uppercase+reversal(string.ascii_uppercase):
        if let > letter:
            continue
        else:
            inside = sum([key for key,val in enumerate(string.ascii_uppercase) if let == val])*2-1
            outside = int((indx - inside)/2) if let != "A" else int((indx - inside)/2)
            if let != "A":
                val = val + [(outside*" ")+let+(inside*" ")+let+(outside*" ")]
            else:
                val = val + [(outside*" ")+let+(outside*" ")]
    return val

def reversal(stringy):
    return "".join(reversed(stringy))