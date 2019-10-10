#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 22:47:35 2019

@author: lakshmanteja
"""
import argparse, sys

from Bio import SeqIO

parser = argparse.ArgumentParser(description='A scripy to read GenBank file and parse its features')
parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')

required = parser.add_argument_group('Required Arguments')
required.add_argument('-i','--input', help='Please enter a Genbank file name')
#required.add_argument('-f','--feature', help='Enter your choices like annotations |dbxrefs | description | features | seq ')

args = parser.parse_args(args=None if sys.argv[1:] else ['-h'])
    
gbk_file = SeqIO.read(open(args.input,'r'), "genbank")

print(gbk_file.annotations["source"])
print("Total featre :" , len(gbk_file.features))
print('Key feature:',gbk_file.features['type'])
#feature_count = 0
#for feat in gbk_file.features:
#    if feat.type == args.feature:
#         feature_count = feature_count + 1
#print((args.feature) + ":" , str(feature_count))
 

