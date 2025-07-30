input_dna_seq = "ACACACACCACTTTTTTTTTT"

""""Function assumes that the input is correct and only ACTG nucleotides are given."""


def dna_converter(dna):
    rna = dna.replace("T", "U")
    print(rna)
    return rna


dna_converter(input_dna_seq)
