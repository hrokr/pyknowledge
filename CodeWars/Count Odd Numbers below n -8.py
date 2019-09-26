def odd_count(n):
    """
Count Odd Numbers below n <8 kyu>

Comments:
    As a side note, md5 can be exploited, so never use it for anything secure.
    The reason I used it in this kata is simply because it is a very common
    hashing algorithm and many people will recognize the name.

Task:
    Given a number n, return the number of positive odd numbers below n, EASY!

Notes:
    Expect large Inputs!

Input >> Output Examples
    oddCount(7)  #==> 3, i.e [1, 3, 5]
    oddCount(15) #==> 7, i.e [1, 3, 5, 7, 9, 11, 13]
    """

    return n//2



"""
Other solutions of mine that worked but CW deemed as too slow
# return len(map(x%2,[x for x in range(1, n)]))
# return sum(map(lambda x: x%2, [x for x in range(1, n)]))
"""


c= odd_count(15023) #,7511)
print(c)
