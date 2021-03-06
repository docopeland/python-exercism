import string

def rows(letter):
    abc = enumerate(string.ascii_uppercase)
    indx = sum([key for key,val in abc if letter == val])*2-1
    val = []
    upto = string.ascii_uppercase.index(letter)
    fullabc = string.ascii_uppercase[:upto+1]+"".join(reversed(string.ascii_uppercase[:upto]))
    for let in fullabc:
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