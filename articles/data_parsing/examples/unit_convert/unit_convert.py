#Bank calc
#goe through a data file and defines 'bank angle' of a road based on its curvature

# open() files for reading and writing
fIn = open('figure_8_meters.rdf', 'r')
fOut = open('figure_8_feet.rdf', 'w')

#initialise a string 'header' to store the non-data
header = ''
#and a matrix to store the data
data = []
data_block = False

for line in fIn:

    # this operation will take place only after the data section starts
    # this flag gets set below
    if data_block:

        # first take the EOL of character off with rstrip()
        # then split the line into an array
        row = line.rstrip().split('\t')

        #lets a string comprehension to turn the strings into numbers
        number_row = [float(x) for x in row]

        # now lets do the conversion
        # note that we only need to perform the operation on the 1st 4 items
        # for we slice syntax and array concatenation
        imperial_row = [x * 3.28 for x in number_row[:3]] + number_row[3:]

        # now lets go back to string to prepare for the file write
        str_row = [str(x) for x in imperial_row]

        #join and write the row, and an windows EOL character
        fOut.write('\t'.join(str_row) + '\n')

    else:
        # write out the string replacing 'meter' with 'feet'
        fOut.write(line.replace('meter', 'feet'))

    # check for the starting character of the line before the data
    if '{    X' in line:
        data_block = True





fIn.close()
fOut.close()
