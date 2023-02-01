import sys
import math
a, b, v = map(int, sys.stdin.readline().split())

days = (v-b)/(a-b)

print(math.ceil(days))