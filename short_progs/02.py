


def rotate(text, offset):
    """
    (str, int) --> (str)

    takes a string, converts it to lower case, rotates each letter by the offset

    rotate('What', 3)
    zkdw

    """

    # return text.lower().encode('rot13')  # works but limited
    result = ''


    for letter in text:
        letter = ord(letter)
        result += (chr((letter + offset)))


    return(result)



out = rotate("This is the super secret text. Donna tella nobody!!", 2)

print(out)
