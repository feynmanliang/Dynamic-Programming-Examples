# 15.4-5: Finding the maximum monotonically increasing sub sequence
# Feynman Liang, 4-4-2012
def findMaxIncreasingSeq(data):
    seqlen = [0] # memoized[i] = len of max seq ending at i
    start = [0] # start index of max seq ending at i
    best = 0

    # iterate across all array elements
    for i in range(1,len(data)):
        if data[i] >= data[i-1]: # if monotonically increasing, add to running seq.
            seqlen.append(seqlen[i-1]+1)
            start.append(start[i-1])
            if seqlen[i] > seqlen[best]:
                best = i
            else:
                seqlen.append(0)
                start.append(i)

    # format return
    print ("input: %s" % str(data))
    print("return: length '%d' between index '%d' and '%d'" % (seqlen[best] + 1, start[best], best))

data = [3, 3 ,9 ,87 ,13 ]
findMaxIncreasingSeq(data)