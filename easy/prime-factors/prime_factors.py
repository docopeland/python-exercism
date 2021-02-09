def factors(value):
    facts = []
    for i in range(2,20):
        if value % i == 0:
            facts = facts + [i]
            value = value / i
    return facts
