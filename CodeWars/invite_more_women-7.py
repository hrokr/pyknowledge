def invite_more_women(arr):
    """
Simple Fun #152: Invite More Women? <7 kyu>

Comments:
    There was a foolish ruse of story not worth repeating. But let's just say
    King Authur would have put Lancelot in his place.

Task:
    return false if -1 values are greater than or equal to 1 values

Notes:
    None

Input >> Output Examples
    invite_more_women([1, -1, 1])   #==>True
    invite_more_women([-1, -1, -1]) #==>False
    invite_more_women([1, -1])      #==>False
    invite_more_women([1, 1, 1])    #==>True
    invite_more_women([])           #==>False
    """

    return arr.count(-1) < arr.count(1)

"""
Other solutions from CW:
    return sum(arr) > 0

"""
c = invite_more_women([1, -1])
print(c)