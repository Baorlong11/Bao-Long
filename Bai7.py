n = int(input("Nhập số nguyên dương n: "))

check = True

while n > 0:
    digit = n % 10
    
    if digit != 6 and digit != 8:
        check = False
        break
    
    n //= 10

if check:
    print("Là số may mắn")
else:
    print("Không phải số may mắn")