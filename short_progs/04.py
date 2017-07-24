#write a program that will print the song "99 bottles of beer on the wall".
#for extra credit, do not allow the program to print each loop on a new line.

# remove the # in the line above the decriment for extra credit.


def bottles_of_beer(bottles):
    while bottles > 0:
        print (bottles, "bottles of beer on the wall.", bottles, "Bottles of beer!\n"
            "Take one down, pass it around ...", bottles -1, "bottles of beer on \n"
            "the wall." #, sep = ' ' )
        bottles -= 1

print(bottles_of_beer(2))
