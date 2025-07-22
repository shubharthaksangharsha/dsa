def mystyle(arr):
    pass #TODO

def find_largest(arr):
    '''
    TC: O(N), SC: O(1)
    '''
    maxi = -1 
    for i in  arr:
        if  maxi <= i: 
            maxi = i
    return maxi 

def find_largest_brute(arr): 
    '''
    TC: O(NlogN), SC: O(1)
    '''
    return sorted(arr)[-1]

if __name__ == '__main__':
    with open('inputf.in', 'r') as infile:
        arr = list(map(int, infile.readline().strip().split()))  # Read and convert to integer list
    # print(find_largest_brute(arr))
    print(find_largest(arr))
