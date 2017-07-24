
fname = raw_input("Please enter the name of the file to parse:  ")

fhand = open(fname)

line_count = 0

for line in fhand:
    #words = line.split()
    #print words[0]
    print line
    line_count = line_count + 1

print "There were " + str(line_count) +  " lines parsed in the file "



"""50	    $56
100	$67	    Save 40%
200	$87	    Save 61%
300	$105	Save 69%
500	$137	Save 76%
1,000	$208	Save 81%
2,000	$330	Save 85%
3,000	$440	Save 87%
5,000	$642	Save 89%
10,000	$1,085"""
