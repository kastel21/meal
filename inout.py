import sys
import os

outfilename = "data.txt"
infilename = 'dataset.txt'
def readlines(filename):
	with open(filename, 'r') as infile:
		return infile.readlines()

def writelines(filename, outstr):
	with open(filename, 'w') as outfile:
		outfile.write(outstr)

def output(outstr):
	writelines(outfilename, outstr)
	
infilelines = readlines(infilename)
