dna_nucleotides = ["A", "C","G"]

input_dna_seq = "acacacttttttttt"

""""Function assumes that the input is correct and only ACTG nucleotides are given."""
def dna_converter(dna_seq):
    rna_seq = ""
    for n in input_dna_seq:
       if n.upper() in dna_nucleotides:
            rna_seq += n.upper()
       else:
           rna_seq += "U"
    print(rna_seq)
    return rna_seq

dna_converter(input_dna_seq)