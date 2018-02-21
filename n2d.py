#CHANGE API KEY LINE 9 TO YOUR OWN FROM CLEARBIT

import io
import os
import json
import argparse
import clearbit

clearbit.key = '****INPUT YOUR OWN API KEY****'

parser = argparse.ArgumentParser()
parser.add_argument("-f",help="Input text file with company names and receive associated domains..",action="store_true")
args=parser.parse_args()

if (args.f):
	infile = input("Location of text file with company names..")
	outfile = input("Location of output text file..")
	fopen = open(outfile, 'w')
	with open(infile) as f:
	    for i in f:
	        x = i.rstrip('\n')
	        name = x
	        print(name+" DONE!")
	        domain = clearbit.NameToDomain.find(name=name)
	        writedomain = domain
	        fopen.write(str(writedomain))
	        fopen.write('\n')
	fopen.close()


	


