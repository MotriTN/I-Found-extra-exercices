r = int(input("N: "))
p=""
for i in range(1, r + 1):
    a = int(input(f"Donner la note n°{i} :"))
    k=a
    pai = 0
    imp = 0
    while k != 0:
        x = k % 10
        if x % 2 == 0:
            pai += 1
        else:
            imp += 1
        k = k // 10 
    if pai>imp:
        p+=str(a)+","
print(p)