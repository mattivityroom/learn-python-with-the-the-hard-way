# This is Python version 2.7.12
# Exercise 17: More Files

# to run this use:
# python ex17.py test.txt new_file.txt

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line, how ?
# indata  = open(from_file).read()
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort"
raw_input()

# open(to_file,'w').write(indata)
out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done"

out_file.close()
in_file.close()