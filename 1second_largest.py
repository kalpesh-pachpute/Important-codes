# method 1
def second_largest(arr):
    unique=sorted(set(arr()))
    if len(unique)<2:
        return None
    return[-2]


# method 2
n = int(input())
arr = list(map(int,input().split()))
uniqu = sorted(set(arr))
if len(uniqu) < 2:
    print(-1)
else:
    print(uniqu[-2])
