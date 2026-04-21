from datetime import datetime

# Thiết lập thời gian giả định theo đề bài
now = datetime.now()

print(f"{'Thông tin cần hiển thị'}: {'Kết quả hiển thị'}")
print("-" * 70)
print(f"{'Năm hiện tại'}: {now.year}")
print(f"{'Tháng hiện tại bằng chữ'}: {now.strftime('%B')}")
print(f"{'Tuần hiện tại là tuần thứ mấy trong năm'}: {now.isocalendar()[1]}")
week_in_month = (now.day - 1) // 7 + 1
print(f"{'Tuần hiện tại là tuần thứ mấy trong tháng'}: {week_in_month}")
print(f"{'Ngày hiện tại là ngày thứ mấy trong năm'}: {now.timetuple().tm_yday}")
print(f"{'Ngày dương lịch hiện tại là ngày'}: {now.day}")
print(f"{'Thứ của ngày hiện tại'}: {now.strftime('%A')}")
print(f"{'Giờ phút giây hiện tại'}: {now.strftime('%H:%M:%S')}")