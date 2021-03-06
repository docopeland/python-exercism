import string

def rows(letter):
    val = []
    indx = string.ascii_uppercase.index(letter)
    fullabc = string.ascii_uppercase[:indx+1]+"".join(reversed(string.ascii_uppercase[:indx]))
    for let in fullabc:
        inside = sum([key for key,val in enumerate(string.ascii_uppercase) if let == val])*2-1
        outside = int((len(fullabc)-inside-2)/2)
        if let != "A":
            val = val + [(outside*" ")+let+(inside*" ")+let+(outside*" ")]
        else:
            val = val + [(outside*" ")+let+(outside*" ")]
    return val