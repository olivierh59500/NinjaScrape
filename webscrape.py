#!/usr/bin/python

import urllib2
import re
import readline

site = raw_input("Enter page: ")

#open site. read so we can read in a string context
data = urllib2.urlopen(site).read()

#run the data through re/regex
patternFile = open('items.dat','r').read().splitlines()
for pattern in patternFile:
	m = re.findall("'"+pattern+"'",data)
	if m:
		#open output/results file...append because we are cool
		outfile = open('RESULTS.txt','a')
		print i
		outfile.write(i)
		outfile.write("\n") #may be needed. can always be removed.
		
		#close the file..or else
		outfile.close()
	else:
		continue

	
