# Validate a telephone number, as if written on an input form.
# Telephone numbers can be written as ten digits, with dashes, spaces, dots
# between the three segments, or with the area code parenthesized
# Both the area code and any white space between segments are optional.

# Examples --  all of the following are valid telephone numbers: 1234567890,
# 123-456-7890, 123.456.7890, (123)456-7890, (123) 456-7890 (note the whitespace
# following the area code), and 456-7890.

# The following are not valid telephone numbers: 123-45-6789, 123:4567890,
# and 123/456-7890. source: programmingpraxis.com


base = input("please enter a number to validate  ")
