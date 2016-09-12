## This may not be the best way to generate it.. 
# I was facinated by the pascal's triangle and wanted to play around with it.. I wanted to test out a few things on the larger scale
# and foudn this code online at http://stackoverflow.com/questions/24093387/pascals-triangle-for-python
# Made a few changes and it now prints it beautifully 

import math,sys

# pascals_tri_formula = [] # don't collect in a global variable.

def combination(n, r): # correct calculation of combinations, n choose k
    return int((math.factorial(n)) / ((math.factorial(r)) * math.factorial(n - r)))

def for_test(x, y): # don't see where this is being used...
    for y in range(x):
        return combination(x, y)

def pascals_triangle(rows):
    result = [] # need something to collect our results in
    # count = 0 # avoidable! better to use a for loop, 
    # while count <= rows: # can avoid initializing and incrementing 
    for count in range(rows): # start at 0, up to but not including rows number.
        # this is really where you went wrong:
        row = [] # need a row element to collect the row in
        for element in range(count + 1): 
            # putting this in a list doesn't do anything.
            # [pascals_tri_formula.append(combination(count, element))]
            row.append((combination(count, element))%5)  ## Change 5 to whatever mod you are interested/ remove it 
        result.append(row)
        # count += 1 # avoidable
    return result

# now we can print a result.. It prints a space if it is 0 and 1 for everything else.. It makes it easier to read the output..

count = 100 ## Prints for 50 rows 
for row in pascals_triangle(100):
    sys.stdout.write(" "*count)
    for i in row:
        if int(i)== 0 :
            sys.stdout.write(" " + " ")
        else:
            sys.stdout.write("1" + " ")
        # sys.stdout.write(str(i) + " ")
    sys.stdout.write("\n")
    count-=1
