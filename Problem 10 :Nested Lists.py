arr=[]
b = set()
for _ in range(int(input())):
    name = input()
    score = float(input())
    b.add(score)
    s = [name , score]
    arr.append(s)
b = list(b)
b.sort()
pp = []
for i in range(len(arr)):
    if b[1] == arr[i][1]:
        pp.append(arr[i][0])
pp.sort()
for j in pp:
    print(j)
