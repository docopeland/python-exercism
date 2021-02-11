def factors(value,start = 2):
    facts = []
    while value > 1:
        if value % start == 0:
            facts.append(start)
            value = value / start
        else:
            start = start + 1
    return facts
