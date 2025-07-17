n , m = map(int , input().split())
x = list(map(int , input().split()))

a = set(map(int , input().split()))
b = set(map(int , input().split()))
h = 0
for i in range(n):
    if x[i] in a:
        h +=1
    if x[i] in b:
        h -=1

print(h)
