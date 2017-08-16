# funct_01.py

name_lengths = map(len, ["Mary", "Isla", "Sam"])

print name_lengths

# This only works in python 2. Python 3 yeilds something like:
# <map object at 0x100b87a20>

#name_lengths = map(len, ["Mary", "Isla", "Sam"])
#print(name_lengths)

# First question -- why is that?
# In Python2, map() returns a list; in Python3, it returns an iterator.

# This simple python 2 script:

'''names = ['Mary', 'Isla', 'Sam']

for i in range(len(names)):
    names[i] = hash(names[i])

print names
'''

# is functionally equilivant to this ...

names = ['Mary', 'Isla', 'Sam']
secret_names = map(hash, names)
print secret_names

# Let's pass in a function using the same list of names above.

def double(name):
    return name + name

doubled_names = map(double, names)
print "doubled is", doubled_names

# Now let try it using a simple lambda

redoubled = map(lambda x: x*2, names)
print "redoubled (aka, my first lambda) is ", redoubled
