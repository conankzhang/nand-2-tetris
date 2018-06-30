import sys
import os

fileIn = open(sys.argv[1], 'r')

fileName = os.path.splitext(fileIn.name)[0]
fileOut = open(fileName + '.hack', 'w')

for line in fileIn:
    fileOut.write(line)