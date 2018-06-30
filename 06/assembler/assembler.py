import sys
import os

file_in = open(sys.argv[1], 'r')

file_name = os.path.splitext(file_in.name)[0]
file_out = open(file_name + '.hack', 'w')

for line in file_in:
    file_out.write(line)
