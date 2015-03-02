__author__ = 't3281j0'

import re

#Spring convert
#Combine the format of coil_spring_100N.xml and the date of coil_spring_50N.spr into a new coil_spring_50N.xml file
f_template = open('coil_spring_100N.xml', 'r')
f_source = open('coil_spring_50N.spr', 'r')
f_destination = open('coil_spring_50N.xml', 'w')



#get the desired data out of the source file
stiffness_data = []
for line in f_source:

    match = re.match('^(-*\d+\.*\d*)\s+(-*\d+\.*\d*)', line)
    # this pattern matches to a line with two number strings (which may or may not start with with '-' and contain '.')

    if match:
        stiffness_data.append(match.groups())   # match.groups() returns a tuple of all matched groups, defined py parenthesis in the pattern


#Loop through the template, detecting the data section and writing the input data instead
data_written = False
for line in f_template:
    number_search = re.match('^\s+(-*\d+\.?\d*)\s+(-*\d+\.?\d*)', line)

    if number_search is None:    # not a data line, transcribe the non-data template line directly
        f_destination.write(line)

    else:

        if not data_written:    # on first detection of the template data, write the source data instead

            for row in stiffness_data:
                f_destination.write('  %s  %s\n' % row)
            data_written = True     # flag for current if statement, prevent multiple writing of source data

        else:   # do nothing if number_search and data_written
            continue






