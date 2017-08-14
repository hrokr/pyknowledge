def increment(a):
    return a + 1

def double(a):
    return a * 2

def together(a):
    return double(increment(a))

print(increment(6))
print(together(6))
