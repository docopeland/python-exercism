SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4

def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    elif listchecker(list_one,list_two):
        return SUBLIST
    elif listchecker(list_two,list_one):
        return SUPERLIST
    else:
        return UNEQUAL

def listchecker(list1:list,list2:list):
    if len(list1) == 0:
        return True
    elif len(list1) > len(list2):
        return False
    else:
        if list2.count(list1[0]) > 0:
            for i in range(len(list1)):
                if list1[i] == list2[i]+list2.index(list1[0]):
                    continue
                else:
                    if list2.count(list1[0]) > 1:
                        start = list2[list2.index(list1[0])+1:]
                        for i in range(len(list1)):
                            if list1[i] == start[i]+start.index((list1[0])):
                                continue
                            else:
                                return False
                    return False
        else:
            return False
    return True
