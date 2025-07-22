from findlargest import find_largest
def better_secondlargest(arr):
    '''
    TC: O(N + M),  SC: O(1)
    '''
    largest = find_largest(arr)
    slargest = -1 
    for i in arr: 
        if i > slargest and i != largest:  
            slargest = i 
    return slargest 

def brute_secondlargest(arr):
    '''
    TC: O(NlogN), SC: O(1)
    '''
    sort_arr = sorted(arr)
    i = len(sort_arr) - 2   
    while i  >= 0:
        if  sort_arr[i] == sort_arr[-1]:
            i -= 1 
            continue 
        else: 
            break


    return sort_arr[i]

if __name__ == '__main__':
    with open('inputf.in', 'r') as infile:
        arr = list(map(int, infile.readline().strip().split()))  # Read and convert to integer list
    # print(brute_secondlargest(arr))
    print(better_secondlargest(arr))
