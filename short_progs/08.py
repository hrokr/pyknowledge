grades = [[assignment1, 90][assignment2, 80][assignment3, 88]]

out = 0

for i in grades:
    out = out + grades[i][i+1]

    print(out)
