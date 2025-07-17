alpha = 'abcdefghijklmnopqrstuvwxyz'
mylist = ['a']
body = []
def print_rangoli(size):
        width = 2*(size-1)
        for i in range(1,size):
            mylist.insert(0 , alpha[i])
            mylist.append(alpha[i])
        s = "-".join(mylist)
        body.append(s)
        for i in range(len(mylist)):
            if len(mylist) != 1:
              mylist.remove(alpha[i])
              mylist.remove(alpha[i+1])
              w = "-".join(mylist)
              w = ((2*(i+1))*"-")+ w + ((2*(i+1))*'-')
              body.insert(0 , w)
              body.append(w)
        for j in body:
              print(j)
