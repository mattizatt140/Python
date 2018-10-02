###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.
    
    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    CowKey = sorted(cows, key=cows.__getitem__, reverse=True); CowVal = sorted(cows.values(), reverse=True)
    totalTransport = []
    while CowKey:
        curWeight = 0; curTransport = []
        while True:
            largest = -1
            for i in range(len(CowVal)):
                if (CowVal[i] >= CowVal[largest]) and CowVal[i] + curWeight <= limit:
                    largest = i
            curWeight += CowVal[largest]
            if curWeight > limit:
                break
            else:
                curTransport.append(CowKey[largest])
                del CowKey[largest]
                del CowVal[largest]
                if not CowKey:
                    break
        totalTransport.append(curTransport)
    return totalTransport
            

# Problem 2
def brute_force_cow_transport(cows,limit=10):
    validPartitions = get_partitions(cows)
    return min(validPartitions, key=len)

        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")

limit = 10
#print(cows)
print(greedy_cow_transport(cows, limit))
print(brute_force_cow_transport(cows, limit))