def distance(strand_a, strand_b):
    if len(strand_a) is not len(strand_b):
        raise ValueError("Strands are not the same length")
    else:
        ham = 0
        for seq in zip(range(len(strand_a)),range(len(strand_b))):
            if strand_a[seq[0]] is strand_b[seq[0]]: continue
            else: ham = ham + 1
        return ham