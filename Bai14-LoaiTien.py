def giai_bai_toan_doi_tien():
    # Nhập số tiền từ bàn phím
    try:
        x_input = int(input("Nhap so tien X: "))
    except ValueError:
        print("Vui long nhap mot so nguyen.")
        return

    # Danh sách 9 loại mệnh giá theo thứ tự từ lớn đến nhỏ
    menh_gia = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    
    # In dòng tiêu đề giống ví dụ
    print(f"So tien {x_input} duoc doi thanh:")
    
    tong_so_to = 0
    con_lai = x_input

    # Duyệt qua từng mệnh giá để tính toán
    for mg in menh_gia:
        so_to = con_lai // mg
        con_lai = con_lai % mg
        tong_so_to += so_to
        
        # In ra số tờ của mỗi loại theo đúng định dạng "Loai [gia] gom [so] to"
        print(f"Loai {mg} gom {so_to} to")
        
    # In dòng tổng cộng ở cuối
    print(f"TONG CONG CO {tong_so_to} TO")

# Gọi hàm thực hiện
giai_bai_toan_doi_tien()