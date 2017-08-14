import random

example = [19, 30, 38, 49, 7*9, 'equals', 63, 89]
superheroes = ['superman', 'batman', 'wonder woman', 'fishboy', 'flash']

double = [2*x for x in example]
hardways = [ (x,x) for x in (2,3,4,50)]
random = [random.random() for x in range(7)]
hero_name_length= [len(name) for name in superheroes]
two_longest = [len(name) for name in superheroes if len(name) > 7]
longish = [name for name in superheroes if len(name) > 7]

print(double)
print(hardways)
print(random)
print(hero_name_length)
print(two_longest)
print(longish)
