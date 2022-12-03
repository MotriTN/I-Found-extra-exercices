date=input("Donner la date JJ/MM/AAAA : ")
JJ=[0,find("/")]
MM=[find('/')+1,find('/')]
AAAA=[(find('/')+1):]
if 1<=JJ<=31 and 1<=MM<=12 and 1950<=AAAA<=2023:
    print("Valide")
else:
    print("Invalide")