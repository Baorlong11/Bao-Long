def ucln(a, b):
    if b == 0:
        return a
    return ucln(b, a % b)

a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
print(f"USCLN cua {a} va {b} la: {ucln(a, b)}")