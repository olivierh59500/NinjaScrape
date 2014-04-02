#!/usr/bin/python

import urllib2
import re
import readline #nice when you need to use arrow keys and backspace
import sys

site = raw_input("Enter page: ")

#open site. read so we can read in a string context
data = urllib2.urlopen(site).read()

#try an open the pattern file. 
try:
	patternFile = open('items.dat','r').read().splitlines()
except:
	print "There was an error opening the items.dat file"
	sys.exit("Encountered some errors")
#for each loop so we can process each specified regex
for pattern in patternFile:
	m = re.findall("'"+pattern+"'",data)
	#m will return as true/false. Just need an if m:
	if m:
		#open output/results file...append because we are cool
		outfile = open('RESULTS.txt','a')
		print i
		outfile.write(i)
		outfile.write("\n") #may be needed. can always be removed.
		
		#close the file..or else
		outfile.close()
	else:
		#Continue the loop if not a match so it can go on to the next sequence
		continue

	
