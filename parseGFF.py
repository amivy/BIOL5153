#! /usr/bin/env python3

import csv
import re
import argparse
from Bio import SeqIO
from collections import defaultdict
 
# inputs: 1) GFF file; 2) corresponding genome sequence (FASTA format)

# define the function get_seq
def get_seq(s, e, str):

    #extract the sequence
    fragment = genome.seq{int(start)-1:int(end)

    #check for +/- strand and return as is or rev-comp
    if(str == '+'):
        return fragment
    else:
        return fragment.reverse_complement()

# create an argument parser object
parser = argparse.ArgumentParser(description='this script will parse a GFF file and extract each feature from the genome')

# add positional arguments
parser.add_argument('gff', help='name of the GFF file')
parser.add_argument('fasta', help='name of the FASTA file')

# parse the arguments
args = parser.parse_args()

# read in FASTA file
genome = SeqIO.read(args.fasta, 'fasta')

# create a dictionary for genes with introns/multiple exons
# key = gene name, value = list of exon sequences
exons = defaultdict(dict)

# open and read in GFF file
with open(args.gff, 'r') as gff_in:
    # create a csv reader object
    reader = csv.reader(gff_in, delimiter='\t')

    # loop over all the lines in our reader object (ie, parsed file)
    for line in reader:
        species = line[0].replace(" ","_")
        feature_type = line[2]
        start = line[3]
        end = line[4]
        strand = line[6]

        #split attribute field in a list
        attr_fields = line[8].split()
        gene_name = attr_fields[1]

        if(feature_type == 'CDS'):
            # search for 'exon' annotation
            match = re.search("exon\S+(\d+)", line[8])

            # test for whether there are multiple exons
            if (match):
                # create FASTA header, which is also the dictionary key for 'exons'
                header = species + "_" + gene_name
                # get the exon number
                exon_number = match.group(1)
                # get the sequence for this exon
                exon = get_seq(int(start)-1:int(end), strand)
                if(header in exons_dict):
                    print('already there')
                   # exons[header] = exon_number
                else:
                    exons_dict[header] = defaultdict(list)
               

            #print genes without introns
            #else:
                #print the FASTA header
               # print(">" + species + '_' + gene_name)
                #extract the sequence
               # print(get_seq(int(start)-1:int(end), strand))
        else:
            continue


        #print(len(genome.seq))
# loop over exons dictionary
for gene, cds in exons_dict.items():
    print('>'+ gene)
    print(cds)
