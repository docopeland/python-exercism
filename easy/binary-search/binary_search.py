def find(search_list:list, value,indx=0):
    half = len(search_list)//2
    if len(search_list) < 1 or (len(search_list) == 1 and search_list[half] != value):
        raise ValueError("Not in series")
    elif search_list[half] == value:
        return indx + half
    elif search_list[half] > value:
        return find(search_list[:half],value,indx)
    elif search_list[half] < value:
        return find(search_list[half:],value,half+indx)
