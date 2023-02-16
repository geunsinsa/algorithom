import sys

n , m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
arr = []

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            comb_sum = nums[i] + nums[j] + nums[k]
            if comb_sum <= m:
                arr.append(comb_sum)
print(max(arr))










