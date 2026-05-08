from datetime import datetime

S = input("Nhập chuỗi ngày: ")

d = datetime.strptime(S, "%b %d %Y %I:%M%p")

print(f"Dữ liệu sau khi chuyển: {type(d)}")
print(f"Giá trị ngày tháng: {d}")