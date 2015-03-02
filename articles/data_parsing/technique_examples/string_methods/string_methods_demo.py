# File are arrays of sting, so naturally,
# the built in method for arrays any strings are critical to data file parsing

# String methods

# there is no str.remove(), use replace instead
print '233.4,  232.33, 342.34'.replace(' ', '')
# >>> 233.4,232.33,342.34

# line from files will have trailing EOL and often padded space chars
# tis can be removes with str.rstrip()
print '  data =  2,3,4,5   \n'.rstrip()
# >>>     data = 2,3,4,5

# lstrip() is the same but for leading chars
print '  data =  2,3,4,5'
# >>> data = 2,3,4,5

# lines can be split into arrays using split()
line = '233.4,232.33,342.34'
print line.split(',')
# >>> ['233.4', '232.33', '342.34']



# string can stacked to perform several operation at once
line = 'center_of_mass =  1.3, 23.4, 23.4  \n'
print line.rstrip().split('=')[1].lstrip().split(',')
# >>> ['1.3', ' 23.4', ' 23.4']


# using split, strip and remove in combinatoin, we get the line "clean"
line = 'center_of_mass =  1.3, 23.4, 23.4  '

