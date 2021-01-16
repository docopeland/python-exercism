def to_rna(dna_strand):
    switch = {"G":"C","C":"G","T":"A","A":"U"}
    return "".join([switch[tide] for tide in dna_strand])