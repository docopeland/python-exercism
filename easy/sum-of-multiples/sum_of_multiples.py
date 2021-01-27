def sum_of_multiples(limit, multiples):
    if 0 in multiples:
        multiples.remove(0)
    return sum(set([ints for ints in range(1,limit) for vals in multiples if ints % vals == 0]))
