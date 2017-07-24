# Create a program that asks the users name, age, and reddit username.
# have it tell them the information back, in the format:

# your name is (blank), you are (blank) years old, and your username is (blank)

# Extra Credit, have the program log this information to a file.




name = input("What is your name?  ")

age = int(input("What is your age?  "))

if age < 0:
    print("That's not a valid number but we'll just move on")

elif age > 110:
    print("Over 110??! I don't think so. Whatever, let's keep going")

username = input("What is your reddit username?  ")

print("Your name is %s, you are %d years old, and your username is %s ." %
      (name, age, username))


line = name + ',' + str(age) + ',' + username + "\n"

with open("01outfile.py", 'a') as out:
    out.write(line)
