word = 'WELCOME'
length , width = map(int,input().split()) 
s = '.|.'
mylist = []
for i in range(int(length/2)):
    w = s * (2*i+1)
    w = w.center(width , "-")
    mylist.insert(i,w)
    mylist.insert(-i-1,w)
word = word.center(width,"-")
mylist.insert(int(length/2),word)
for k in  mylist:
    print(k)
