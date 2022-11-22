ch=input("Give ch : ")
b=True
a=True
for i in range (len(ch)-1):
    if (int(ch[i+1]))<(int(ch[i])) :
        b=False
    elif (int(ch[i+1]))>(int(ch[i])) :
        a=False
    elif (int(ch[i+1]))==(int(ch[i])):
        b=False
        a=False
if b == (True or a==True) and len(ch)>1 :
    print("They're sorted")
elif len(ch)==1:
    print("This Number can't be sorted") 
else : 
    print("They're not sorted")