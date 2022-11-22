r = int(input("donner le nombre des notes : "))
z = 0
l=[]
f=0
b=0
for i in range(1, r + 1):
    a = float(input(f"Donner la note n°{i} :"))
    z = z + a
    l.append(a)
    s=l.count(a)
    if s>f:
        f=s
        b=a
    if s==f and a>b:
        f=s
        b=a
p=sorted(l)
print("le moyen est:", z / r)
print(f"le nombre le plus repeté est {b} de {f} fois ")
print(f"la liste des nombres est : {p[::-1]} ")