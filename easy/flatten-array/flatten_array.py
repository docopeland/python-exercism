def flatten(iterable):
    val = []
    for i in iterable:
        if type(i) is int:
            val = val +[i]
        elif i is not None:
            val = val +flatten(i)
    return val
