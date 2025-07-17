n = int(input())
a = set(map(int , input().split()))
m = int(input())
b =set(map(int,input().split()))

s = a.symmetric_difference(b)
s = list(s)
s.sort()
for i in s:
    print(i)
