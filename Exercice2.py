r=int(input("Give a : "))
n=int(input("Give b : "))
l1=[]
l2=[]
z=0
j=0
for i in range (len(str(r))):
    z=r%10
    l1+=z
    z=r//10