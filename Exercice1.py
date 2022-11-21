n=int(input("Give n :")) #1234 or 4321
l=len(str(n))
z=1
j=1
a,b=False,False
i=0
while not j==0 and not i==(l-1):
    i+=1
    z=n%10
    j=((n//10)%10)
    print(j)
    if z>j:
        a=True
        n//=10
    elif j>z :
        b=True
        n//=10
    elif z==j:
        a=True
        b=True
else:
    if (a,b)==(True,True):
        print("This number is bad")
    elif (a,b)==(True,False):
        print("This number is ascending")
    elif (a,b)==(False,True):
        print("This number is descending")