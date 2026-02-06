# method 1
def unique_pair(arr,k):
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == k:
                count += 1
        return count
    

# method 2
def unique_pair(arr, k):
    seen = set()
    count = 0
    for num in arr:
        if(k-num) in seen:
            count += 1
        seen.add(num)
    return count
