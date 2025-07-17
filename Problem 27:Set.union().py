n = int(input())
s1 = list(map(int, input().split()))
m = int(input())
s2= list(map(int,input().split()))

s1.extend(s2)
s = set(s1)
print(len(s))
