def giai_bai_toan_20():
    try:
        a = int(input("Nhap so tien hang can tra (a): "))
        b = int(input("Nhap so tien khach thuc te tra (b): "))
    except ValueError:
        print("Vui long nhap so nguyen hop le.")
        return
    if a > b:
        print(f"So tien khach hang con thieu la: {a - b}")
    elif a == b:
        print("Cam on khach hang. Hen gap lai")
    else:
        x = b - a
        print(f"So tien {x} duoc doi thanh:")
        menh_gia = [500, 200, 100, 50, 20, 10, 5, 2, 1]
        tong_so_to = 0
        tong_so_loai = 0 
        for mg in menh_gia:
            so_to = x // mg
            x = x % mg
            if so_to > 0:
                print(f"Loai {mg} gom {so_to} to")
                tong_so_to += so_to
                tong_so_loai += 1
        print(f"TONG CONG CO {tong_so_to} TO")
        print(f"Tong so loai = {tong_so_loai}")
        input("\nNhan phim Enter de ket thuc...")
        print("Cam on khach hang. Hen gap lai")
giai_bai_toan_20()