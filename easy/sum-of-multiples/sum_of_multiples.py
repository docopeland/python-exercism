def sum_of_multiples(limit, multiples):
    return sum(set([ints for ints in range(1,limit) for vals in multiples if (vals !=0) and (ints % vals == 0) ]))
