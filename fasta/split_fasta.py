#!/usr/bin/env python
#File created on October 28, 2015

from __future__ import print_function
"""
"""

__author__ = "Migun Shakya"
__email__ = "microbeatic@gmail.com"
__version__ = "0.1"
__license__ = "The MIT License (MIT)"


#--- standard library imports
import argparse
import os

#--- third-party imports
from Bio import SeqIO
#--- project specific imports


def cmdline_parser():
    """
    creates an argparse instance
    """
    parser = argparse.ArgumentParser(description="""split fasta with multiple sequence to fasta with one sequence
        the new fasta are named based on their sequence id""")
    parser.add_argument("-i", "--INPUT",
                        help="""fasta file""",
                        required=True)
    parser.add_argument("-o", "--OUT_FOLDER", help="""output FOLDER""")
    return parser


def main():
    """
    The main function
    """
    parser = cmdline_parser()
    args = parser.parse_args()

    sequences = SeqIO.parse(args.INPUT, 'fasta')

    fasta_list = []
    for record in sequences:
        out_file = os.path.join(args.OUT_FOLDER, record.id + ".fna")
        SeqIO.write(record, out_file, 'fasta')


if __name__ == '__main__':
    main()
