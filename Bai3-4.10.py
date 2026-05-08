s = input("Nhập số điện thoại (S): ")
full_digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
s_digits = set(s)
missing_digits = sorted(list(full_digits - s_digits))

print(f"Trong số điện thoại {s} không chứa các ký số: {missing_digits}")