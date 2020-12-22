def firstFit(length, n, c): 
    res = 0  
    bin_rem = [0]*n 

    for i in range(n): 
        j = 0 
        min = c + 1 
        bi = 0 
        for j in range(res): 
            if (bin_rem[j] >= length[i] and bin_rem[j] - length[i] < min): 
                bi = j 
                min = bin_rem[j] - length[i] 
        if (min == c + 1): 
            bin_rem[res] = c - length[i] 
            res += 1 
        else:
            bin_rem[bi] -= length[i] 
    return res 
if __name__ == '__main__': 
    length = [ 2, 5, 4, 7, 1, 3, 8 ] 
    c = 10 
    n = len(length) 
    print("Number of bins required in First Fit : ", firstFit(length, n, c))