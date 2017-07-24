# Create a random password generator!
# Allow the user to specify the amount of passwords to generate.
# Extra credit: allow user to specify the length of the strings generated

import random


def get_key_params():
    '''
    () --> int, int, str
    #  returns a set to be used as a seed for encryption
    '''

    count = 0
    result = ""

    keys_to_be_generated = int(input('How many keys would you like generated?  '))
    key_length = int(input('How long would you like the keys to be?  '))

    test = input("Select from the following: \n\n(u)pper, (l)ower, (n)umbers,\n"
          "(alpha)numeric, (full)")

    u = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    l = "abcdefghijklmnopqrstuvwxyz"
    n = "1234567890"
    alpha = u + l + n
    s = "!@#$%^&*()/\|{}[]+=<>,.?"
    full = alpha + s

    return keys_to_be_generated, key_length, test


def generate_keys(keys_to_be_generated, key_length, seed_set):
    ''' () -->

    return the
    '''
    keys = []

    while keys < keys_to_be_generated:
        #generate key
        key.append()



#putting it together

get_key_params


# testing
print("keys to be generated are ", keys_to_be_generated)
print("keys length should be ", key_length)
print("option selected was ", result)
print("that turns out to be %s" % result)
