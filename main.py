# def getLargestNumber(num: str) -> str:
#     # Convert to list for efficient swapping
#     nums = list(map(int, num))
#     n = len(nums)
    
#     # Single pass to optimize
#     for i in range(n-1):
#         # Get current digit's parity
#         curr_parity = nums[i] % 2
        
#         # Find largest digit with same parity in remaining part
#         max_digit = nums[i]
#         max_idx = i
        
#         # Search in remaining part of array
#         j = i + 1
#         while j < n:
#             if nums[j] % 2 == curr_parity:
#                 # Check if all intermediate numbers have same parity
#                 can_swap = all(nums[k] % 2 == curr_parity for k in range(j-1, i-1, -1))
#                 if can_swap and nums[j] > max_digit:
#                     max_digit = nums[j]
#                     max_idx = j
#             j += 1
        
#         # Perform swaps to bring the largest digit to current position
#         if max_idx != i:
#             for k in range(max_idx, i, -1):
#                 nums[k], nums[k-1] = nums[k-1], nums[k]
    
#     return ''.join(map(str, nums))
def getLargestNumber(num: str) -> str:
    # Convert to list for manipulation
    nums = list(map(int, num))
    n = len(nums)
    
    # Single pass optimization
    for i in range(n-1):
        curr_parity = nums[i] % 2
        max_digit = nums[i]
        max_idx = i
        
        # Only look for larger numbers with same parity
        for j in range(i + 1, n):
            if nums[j] % 2 == curr_parity and nums[j] > max_digit:
                max_digit = nums[j]
                max_idx = j
        
        # Single swap instead of multiple swaps
        if max_idx != i:
            nums[i], nums[max_idx] = nums[max_idx], nums[i]
    
    return ''.join(map(str, nums))
print(getLargestNumber("7596801"))  # "9758601"
print(getLargestNumber("0082663"))  # "8662003"
print(getLargestNumber("0082"))  # "8662003"