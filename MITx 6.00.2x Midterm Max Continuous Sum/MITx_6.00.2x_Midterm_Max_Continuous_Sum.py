def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    # List to test sum from each element
    maxSum = 0
    for i in range(len(L)):
        sum = 0
        for j in range(i, len(L)):
            sum += L[j]
            if sum > maxSum:
                maxSum = sum
    return maxSum

print(max_contig_sum([3,4,-1,5,-4]))