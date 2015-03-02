# The regular expression language has powerful string matching capabilities
# It's python implementation is called 're'
import re

# The re module has a function search() which takes a reqular expression and the sting to be searched
hay_stack = "hay hay hay needle hay"
pattern = 'n\w'   # pattern reads 'n followed by a wordchar (letters or an underscore)"
match = re.search(pattern, hay_stack)
print match
# >>> <_sre.SRE_Match object at 0x...


# This just confirms that match is in fact an object
# TO see if The object can be used like a boolean

if match:
    print 'Found it'
# >>> Found it
    # To get the portion of the string that matched:
    print match.group(0)
    # >>> ne

# Now we use a term quantifier '+' meaning on or more
print re.search('n\w+', 'hay needle hay').group(0)
# >>> needle

# Finall returns all matches in a string
print re.findall('n\w+', 'needle hay needle hay hay')
# >>> ['needle','needle']

# note that findall returns a array, not an object,
# so the group() method is not required

# Now suppose we want and word stringA starting with 'n or f'
print re.findall('[nf]\w+', 'hay fork hay needle')
# >>> fork, needle

# Or anything but with a letter after h
print re.findall('[^h]\w+', 'spoon hay fork hay needle')
# >>> ['ay', ' fork', ' hay', ' needle']

# Not exactly what we wanted
# Lets add a term to grab whitespace before the 'not n'
print re.findall('\s[^h]\w+', 'hay fork hay needle')

# the output now contains a space
# which we need for a postiive match, but don't want in out results
# lets use grouping to delineate pattern from output
print re.search('\s(\w+)\s', 'hay needle hay').group(1)
# >>> needle
# note how we used group(1) instead of 0, number above zero correspond to groups

#there can be many groups
print re.search('\s([^h])(\w+)\s', 'hay needle hay').group(1)
# >>> n
print re.search('\s([^h](\w+))\s', 'hay needle hay').group(2)
# >>> eedle

#the method groups() returns all groups above 0
print re.search('\s([^h])(\w+)\s', 'hay needle hay').groups()
# >>> ['n','eedle']

# groups can be nested (numbering goes by leading parenthesis only)
print re.search('\s([^h](\w+))\s', 'hay needle hay').groups()
# >>> ['n','eedle']

# findall works with groups too
print re.findall('\s[^h]\w+\s', 'hay hay needle hey fork hey')      # no groups findall
# >>> [' needle ', ' fork ']
print re.findall('\s([^h]\w+)\s', 'hay hay needle hey fork hey')    # single group findall
# >>> ['needle', 'fork']
print re.findall('\s([^h])(\w+)\s', 'hay hay needle hey fork hey')  # multi-group findall
# >>> [('n', 'eedle'), ('f', 'ork')]


# /d is the term for numbers
print re.search('\d+', 'mass = 23.00').group(0)
# >>> 23

# but number strings can contain character other than digits,
# so put multiple terms in brackets and put our + quantifier outside
print re.search('[\d\.]+', 'mass = 23.00').group(0)

# taking it further we can even catch scientific notation
print re.search('(\w+)\s*=\s*([\d\.Ee\+-]+)', 'mass = 1.2934E+09').groups()
# >>> ('mass', '1.2934E+09')

# by combining search() and findall, we can quickly breakdown complex string into 'pure' data
line = 'INERTIA = 4.00E+00     1.32E+01  4.00E-00'
match = re.search('(\w+)\s*=(.*)', line)
print match.groups()
numbers = re.findall('[\d\.Ee\+-]+', match.group(2))
print numbers
# >>> ['4.00E+00', '1.32E+01', '4.00E-00']

# Once strings are decomposed fully, we can easily type cast, manipulate, and build new strings
scale_factor = 1.2
ixx, iyy, izz = [float(x) * scale_factor for x in numbers]
print 'INERTIA = %12.4f %12.4f %12.4f' % (ixx, iyy, izz)   # see topic 'string formatting'
# >>> INERTIA =       4.8000      15.8400       4.8000