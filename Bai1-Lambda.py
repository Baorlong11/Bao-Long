import math

tri_tuyet_doi = lambda n: abs(n)
print("a) Tri tuyet doi:", tri_tuyet_doi(-10))

cong_15 = lambda n: n + 15
print("b) n + 15:", cong_15(10))

tich_hai_so = lambda x, y: x * y
print("c) Tich x va y:", tich_hai_so(5, 6))

la_boi_so = lambda n: n % 13 == 0 or n % 19 == 0
print("d) Boi cua 13 hoac 19:", la_boi_so(39))

dt_hinh_tron = lambda r: math.pi * r**2
print("e) Dien tich hinh tron:", dt_hinh_tron(5))

cv_hinh_chu_nhat = lambda d, r: (d + r) * 2
print("f) Chu vi hinh chu nhat:", cv_hinh_chu_nhat(4, 5))

la_so_chinh_phuong = lambda n: n >= 0 and math.isqrt(n)**2 == n
print("g) So chinh phuong:", la_so_chinh_phuong(16))

la_so_nguyen_to = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1))
print("h) So nguyen to:", la_so_nguyen_to(17))

loai_tam_giac = lambda a, b, c: (
    "Tam giac Deu" if a == b == c else
    "Tam giac Can" if a == b or b == c or a == c else
    "Tam giac Vuong" if (round(a**2 + b**2, 2) == round(c**2, 2)) or 
                        (round(a**2 + c**2, 2) == round(b**2, 2)) or 
                        (round(b**2 + c**2, 2) == round(a**2, 2)) else
    "Tam giac Thuong"
) if (a + b > c and a + c > b and b + c > a) else "Khong phai tam giac"
print("i) Loai tam giac:", loai_tam_giac(3, 4, 5))








