#! /usr/bin/env python3
# set the name of input DNA sequence file
input = 'nad4L.fasta'

# open the input file
infile = open(input,'r')
dna_seq = infile.read().rstrip()
seq_length = len(dna_seq)

# calculate frequencies for each nucleotide
freq_A = dna_seq.count('A')/seq_length
freq_G = dna_seq.count('G')/seq_length
freq_T = dna_seq.count('T')/seq_length
freq_C = dna_seq.count('C')/seq_length

# calculate GC content
GC_content = freq_G + freq_C

# check that frequencies add to 1 - if not, something is wrong
freq_sum = freq_A + freq_G + freq_C + freq_T
print("This is to check that the sum of all AGCT is", str(freq_sum))

# close file
infile.close()

# create the outfile
outfile = open('STDOUT','w')
outfile.write('Sequence length:'+ str(seq_length) + 'nt' + "\n" 
'Freq of A:' + str(freq_A) + "\n"
'Freq of C:' + str(freq_C) + "\n"
'Freq of G:' + str(freq_G) + "\n"
'Freq of T:' + str(freq_T) + "\n"
"G+C content:" + str(GC_content)
)
outfile.close()