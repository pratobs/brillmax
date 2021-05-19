def firstFit(length, n, c):
     
    # Initialize result (Count of bins)
    res = 0
 
    # Create an array to store
    # remaining space in bins
    # there can be at most n bins
    bin_rem = [0]*n
 
    # Place items one by one
    for i in range(n):
         
        # Find the first bin that
        # can accommodate
        # length[i]
        j = 0
         
        # Initialize minimum space
        # left and index
        # of best bin
        min = c + 1
        bi = 0
 
        for j in range(res):
            if (bin_rem[j] >= length[i] and bin_rem[j] -
                                       length[i] < min):
                bi = j
                min = bin_rem[j] - length[i]
             
        # If no bin could accommodate length[i],
        # create a new bin
        if (min == c + 1):
            bin_rem[res] = c - length[i]
            res += 1
        else: # Assign the item to best bin
            bin_rem[bi] -= length[i]
    return res
 
# Driver code
if __name__ == '__main__':
    length = [ 2, 5, 4, 7, 1, 3, 8 ]
    c = 10
    n = len(length)
    print("Number of bins required in First Fit : ",
                             firstFit(length, n, c))
     
# This code is contributed by Rajput-Ji