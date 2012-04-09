# 15-8: Image compression by seam carving
# Feynman Liang, 4-5-2012
import sys
d = [[3,4,5],
     [7,1,5],
     [1,9,9]] # disruption matrix
costMatrix = []
solnMatrix = []

# calculates the least disruptive pair by linking current row with least disruptive legal
# path from previous row
for row in range(len(d)):
    costs = []
    solns = []
    length = len(d[row])
    if row == 0: # base case, 0th row
        costs.append(length)
        solns.append([-1 for entry in range(length)])
    else:
        for k in range(length): # 3 possible cases (best is l, c, or r)
            best = sys.maxint
            if k > 0:
                best = d[row-1][k-1]
                index = k-1
            if d[row-1][k] < best:
                best = d[row-1][k]
                index = k
            if k < length-1 and d[row-1][k+1] < best:
                best = d[row-1][k+1]
                index = k+1
            costs.append(best + d[row][k])
            solns.append(index)
    costMatrix.append(costs)
    solnMatrix.append(solns)

# prints solution by retracing solnMatrix from bottom up
pathMatrix = [[0 for x in range(len(d[0]))] for y in range(len(d))]
soln = min(costMatrix[len(costMatrix)-1])
index = costMatrix[len(costMatrix)-1].index(soln)
for i in reversed(range(0,len(d))):
    pathMatrix[i][index] = '*'
    index = solnMatrix[i][index]

print("Minimum disrupton: %d" % soln)
for row in pathMatrix:
    print row