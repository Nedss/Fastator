"""

Fastator : Random Fasta generator
By Nicolas SOIRAT
Version 1.1.0

"""

#######################################
# IMPORT
#######################################

import random
import argparse

#######################################
# PARSER
#######################################

PARSER = argparse.ArgumentParser()
PARSER.add_argument("-l", "--length", dest="length", default=500,
                    help="Set sequence length (INTEGER)", type=int)
PARSER.add_argument("-n", "--number", dest="number", default=1,
                    help="Set number of sequences in file (INTEGER)", type=int)
PARSER.add_argument("-c", "--character", dest="character", default=60,
                    help="Set character by lines (INTEGER)", type=int)
PARSER.add_argument("-o", "--ouput", dest="output", default="",
                    help="Ouput path")
ARGS = PARSER.parse_args()

#######################################
# FUNCTIONS
#######################################


def rand_seq(length, number):

    """
    INPUT : length of the sequence (parser)
    OUTPUT : list of character
    Generate random list of A, T, C, G
    """

    nucleotide_list = ['A', 'T', 'C', 'G']
    cpt_number = 0
    rand_list = []
    while number > cpt_number:
        cpt_length = 0
        random_sequence = ""
        while length > cpt_length:
            random_char = random.choice(nucleotide_list)
            random_sequence += random_char
            cpt_length += 1
        rand_list.append(random_sequence)
        cpt_number += 1
    return rand_list


def write_fasta(rand_list, character, output):

    """
    INPUT : rand list from previous function
            number of character by lines
    OUTPUT : fasta file
    Generate fasta file
    """

    cpt_number = 1
    with open(output + "random.fasta", 'w+') as random_fasta:
        for sequence in rand_list:
            cpt_char = 0
            random_fasta.write("> Random Sequence " + str(cpt_number) + '\n')
            for nucl in sequence:
                cpt_char += 1
                if cpt_char == character:
                    random_fasta.write(nucl + '\n')
                    cpt_char = 0
                else:
                    random_fasta.write(nucl)
            cpt_number += 1
            random_fasta.write('\n')


#######################################
# MAIN
#######################################


def main():

    """
    Classical main function
    """

    length = ARGS.length
    number = ARGS.number
    character = ARGS.character
    output = ARGS.output

    rand_list = rand_seq(length, number)
    write_fasta(rand_list, character, output)


if __name__ == "__main__":
    main()
