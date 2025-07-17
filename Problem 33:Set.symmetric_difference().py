n = int(input())
a = set(map(int , input().split()))
m = int(input())
b =set(map(int,input().split()))

s = a.symmetric_difference(b)
print(len(s))
