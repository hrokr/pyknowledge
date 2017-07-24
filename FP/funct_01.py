# funct_01.py

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
