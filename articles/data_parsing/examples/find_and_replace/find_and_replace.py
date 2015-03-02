# Find and Replace
# Creates output.txt which is a copy of input.txt except with 'brown' replaced with 'blue'

# open() files for reading and writing
fIn = open('blue.txt', 'r')
fOut = open('brown.txt', 'w')

# any 'iterable' object can be looped by:
for line in fIn:

    # string replace operation
    line = line.replace('blue', 'brown')

    # file write operation
    fOut.write(line)


# close the files
fIn.close()
fOut.close()
