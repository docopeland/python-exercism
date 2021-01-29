SUBLIST = 1
SUPERLIST = 1
EQUAL = 1
UNEQUAL = 1


def sublist(list_one, list_two):
    if list_one in list_two:
        if list_two in list_one:
            return EQUAL
        return SUBLIST
    if list_two in list_one:
        return SUPERLIST
    else:
        return UNEQUAL