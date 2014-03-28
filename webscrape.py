#!/usr/bin/python

import urllib2
import re
import readline

site = raw_input("Enter page: ")

#open site. read so we can read in a string context
data = urllib2.urlopen(site).read()

#run the data through re/regex
m = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',data)

#open output/results file...append because we are cool
outfile = open('RESULTS.txt','a')
for i in m:
	print i
	outfile.write(i)
	outfile.write("\n") #may be needed. can always be removed.

#close the file..or else
outfile.close()

	
