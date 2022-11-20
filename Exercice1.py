n=int(input("Give the number : "))
b=n
c=True
if n//10 > n%10: #4321
    r=True #tasa3oudi
elif n//10 < n%10: #1234
    r=False #tanezouli
else :
    c=False
while c==True:
    if n//10 > n%10 and r==True: #4321 
        n//=10
    elif n//10 < n%10 and r==False : #1234
        n//=10
    else:
        c=False
        if r==True:
            print("Ascending")
        elif r==False:
            print("Descending")
        else:
            print(f"the number {b} is not porte bonheur")
else:
    print(f"there is a draw in the number {b}")