def min_number(input_list):
    """
Form The Minimum <7kyu>

Comments:
    A list is passed in; not a set as the example shows below

Task:
    Given a list of digits, return the smallest number that could be formed from
    these digits,using the digits only once (ignore duplicates).

Notes:
    Only positive integers will be passed to the function (> 0 ), no negatives
    or zeros.

Input >> Output Examples
    minValue ({1, 3, 1})  ==> return (13)
    minValue({5, 7, 5, 9, 7})  ==> return (579)
    minValue({1, 9, 3, 1, 7, 4, 6, 6, 7}) return  ==> (134679)
    """
    
    sorted_list = (sorted(list(set(input_list))))
    return int(''.join([str(x) for x in sorted_list]))

c = [4, 8, 1, 4]
d = min_number(c)
print(d)


"""
Other solutions from CW:

    minValue = lambda a: int(''.join(sorted(str(c) for c in set(a))))

    return int("".join(str(x) for x in sorted(set(digits))))

"""