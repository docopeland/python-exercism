def primes(limit):
    p = list(range(2,limit+1))
    for i in range(2,limit+1):
        for k in range(i+i,limit+1,i):
            if k in p:
                p.remove(k)
    return p
