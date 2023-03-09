# You are given a string S.
# Your task is to print all possible combinations, up to size k , 
# of the string in lexicographic sorted order.

from itertools import combinations
strng,no = input().split()
strng = list(strng)
no = int(no)
strng.sort()
for i in range(1,no+1):
    for wrd in combinations(strng,i):
        print(''.join(wrd))

    

