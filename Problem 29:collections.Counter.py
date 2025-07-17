from collections import Counter
n = int(input())
s = list(map(int , input().split()))
m = int(input())
s = Counter(s)

count = 0
for _ in range(m):
    a , b = map(int , input().split())
    if a in s.keys() and s[a] > 0 :
        s[a] -= 1
        count += b

print(count)
