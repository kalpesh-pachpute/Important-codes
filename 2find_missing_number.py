def find_missing_no (arr):
    n = len(arr) + 1
    expexted_sum = n*(n+1)//2
    actual_sum = sum(arr)
    return expexted_sum - actual_sum
    