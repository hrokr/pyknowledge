
def getSlope(p1, p2):
    """
name <7 kyu>

Comments:
    

Task:
    Each point that the function takes in is an array 2 elements long. The
    first number is the x coordinate and the second number is the y 
    coordinate. If the line through the two points is vertical or if the
    same point is given twice, the function should return null/None.

Notes:
    

Input >> Output Examples

    test.it("Should calculate the existing non-zero between 2 points")
    test.assert_equals(getSlope([1,1],[2,2]), 1, "Incorrect Slope")
test.assert_equals(getSlope([11,1],[1,11]), -1, "Incorrect Slope")
    # okay
    test.it("Should return None if the line passing through the points is vertical")
    test.assert_equals(getSlope([1,1],[1,2]), None, "Incorrect Slope")
    # okay
    test.it("Should return None if the same point is given twice")
    test.assert_equals(getSlope([1,1],[1,1]), None, "Incorrect Slope" 
    """

    return None if p1[1]-p1[0] == 0 or p2[1]-p2[0] == 0 or p1 == p2 else p1[1]-p1[0]/p2[1]-p2[0]




c = getSlope([1,1],[1,1])
print (c)

"""
Other solutions from CW:


"""