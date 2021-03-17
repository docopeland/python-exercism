def find(search_list:list, value):
    if value in search_list:
        return search_list.index(value)
    else:
        raise ValueError("Not in list")
