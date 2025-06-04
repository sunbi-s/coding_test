import sys
import itertools

N, M = map(int,sys.stdin.readline().split())

chars = [i for i in range(1,N+1)]

perm = itertools.permutations(chars, M)
for nums in perm:
    print(*nums)