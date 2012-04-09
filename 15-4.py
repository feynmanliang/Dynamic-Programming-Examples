# 15-4: Printing neatly
# Feynman Liang, 4-4-2012
import sys
##
## Function definitions
##
def printNeatly(text, M):
    text = text.split()

    # memoization/solution tracking grid
    a = generateGrid(text)
    s = generateGrid(text)

    lowestError(text, 0, len(text), M, a,s)
    printSoln(s, a, text)

def generateGrid(text):
    """
    Generates a square grid with dimensions = number words in text
    """
    grid = []
    for i in range(len(text)+1):
        row = []
        for j in range(len(text)+1):
            row.append(0)
        grid.append(row)
    return grid

def lowestError(text, i, j, M, a,s):
    """
    Returns least amount of extra white space required to fit text[i..j] onto
    column width M. a[i][j] = lowest amount of free space fitting text[i..j].
    s[i][j] = position to insert line break which leads to a[i][j], i<s<j
    """
    linelength = 0
    for index in range(i, j):
        linelength += len(text[index])
    linelength += -i +(j)

    # base case - don't need to add line break
    if (linelength <= M) or i>=(j-1):
        if j == len(text): # don't count last line
            return 0
        return (M - linelength) ** 3
    # find optimal line break position using memoized recursion
    best = sys.maxint
    bestindex = 0
    for k in range(i+1,j):
        if a[i][k] > 0:
            error = a[i][k]
        else:
            error = lowestError(text, i,k, M, a,s)
        if a[k][j] > 0:
            error += a[k][j]
        else:
            error2 = lowestError(text,k,j, M, a,s)
            error += error2
        if error < best:
            best = error
            bestindex = k
    totalerror = lowestError(text, i, bestindex, M, a,s) + lowestError(text, bestindex, j, M, a,s)
    a[i][j] = totalerror # memoize
    s[i][j] = bestindex # save solution
    return totalerror

def printSoln(s,a,text):
    if showDebug:
        print "Memoized Subproblem Space Table:"
        for row in a:
            print row
        print '---'

        print 'Optimum Subproblem Solution Table:'
        for row in s:
            print row
        print '---'
    print 'Formatted Text:'
    i = 0
    j = len(text)
    while True:
        k = s[i][j]
        if k == 0:
            print ' '.join(text[i:j])
            break
        print ' '.join(text[i:k])
        i = k
    return

##
## Enter parameters here
##
text = "This is some example sentence"
showDebug = True
printNeatly(text,9)