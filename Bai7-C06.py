import math

def la_so_nguyen_to(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True

def main():
    danh_sach = []
    
    while True:
        num = int(input("Nhập số: "))
        danh_sach.append(num)
        if input("Tiếp tục? (y/n): ").lower() != 'y': 
            break

    # a)
    print("Số nguyên tố:", [x for x in danh_sach if la_so_nguyen_to(x)])

    # b)
    am = [x for x in danh_sach if x < 0]
    duong = [x for x in danh_sach if x > 0]
    print("TBC số âm:", sum(am)/len(am) if am else 0)
    print("TBC số dương:", sum(duong)/len(duong) if duong else 0)

    # c)
    print("Max:", max(danh_sach), "| Min:", min(danh_sach))

    # d)
    check_tang_dan = lambda lst: all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
    print("Đã sắp xếp tăng dần:", check_tang_dan(danh_sach))
    #check_tang_dan = lambda lst: "Đã sắp xếp tăng dần" if lst == sorted(lst) else "Chưa sắp xếp tăng dần"
    #print(f"d) {check_tang_dan(danh_sach)}")
if __name__ == "__main__":
    main()