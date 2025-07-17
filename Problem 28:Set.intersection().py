n = int(input())
s1 = set(map(int, input().split()))
m = int(input())
s2= set(map(int,input().split()))

s = s1.intersection(s2)
print(len(s))
