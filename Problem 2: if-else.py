n = int(input())
if n%2!=0  and n>0:
    print("Weird")
else:
    if n in range(2,6):
        print("Not Weird")
    elif n in range(6,21):
        print("Weird")
    else:
        print("Not Weird")
