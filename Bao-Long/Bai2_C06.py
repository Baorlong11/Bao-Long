from collections import Counter

s1 = input("Nhập S1: ")
s2 = input("Nhập S2: ")

# a)
c1 = Counter(s1)
c2 = Counter(s2)
giao = c1 & c2
print("a) Ký tự chung:", list(giao.keys()))

# b)
print("b) Tổng số ký tự khác biệt:", len(s1_khong_s2) + len(s2_khong_s1))

# c) 
d1 = {char: None for char in s1}
d2 = {char: None for char in s2}
s1_khong_s2 = [c for c in d1 if c not in d2]
s2_khong_s1 = [c for c in d2 if c not in d1]
print("c) Chỉ có ở S1:", s1_khong_s2)
print("   Chỉ có ở S2:", s2_khong_s1)

