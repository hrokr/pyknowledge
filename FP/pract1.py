# Use this:

import random
names = ['Mary', 'Isla', 'Sam']
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']

# And refactor this:

#for i in range(len(names)):
#    names[i] = random.choice(code_names)

#print names
# => ['Mr. Blonde', 'Mr. Blonde', 'Mr. Blonde']

out = map(lambda names: random.choice(['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']),
        names)

print out

# -------------------  Example 2 ------------------

#Use this:

names = ['Mary', 'Isla', 'Sam']

# And refactor this:

#for i in range(len(names)):

#    names[i] = hash(names[i])

print names
# => [6306819796133686941, 8135353348168144921, -1228887169324443034]

out2 = map(hash, names)
print out2
