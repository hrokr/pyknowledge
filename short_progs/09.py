"""
One well known palindrome is "Madam, I'm Adam". Also, there can be numerical palindrome such as 2009002. Most palindrome checkers don't allow for this so ...

Edge cases FTW
"""


def palindrome(phrase):
    distilled = []
    phrase = phrase.lower()

    for char in phrase:
        if char.isalnum() is True:
            distilled.append(char)

    forward = ''.join(distilled)
    backwards = forward[::-1]

    if forward == backwards:
        print phrase + " is a palindrome \n"
    else:
        print phrase + " isn't a palindrome\n"


palindrome("this is a TESt case")
palindrome("This miGHTn't be Too hard!")
palindrome("this2009")
palindrome("Madam, I'm Adam")
palindrome("2002")
palindrome("Abba")
