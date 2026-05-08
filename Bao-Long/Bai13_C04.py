chuoi_chua_hoan_chinh = """
    Quê   hương
Quê  hương  là   chùm  khế   ngọt .
   Cho  con  trèo  hái   mỗi  ngày   .  
Quê   hương  là   đường  đi  học .
  Con  về   rợp  bướm   vàng  bay  .
  Đỗ     Trung  Quân   
"""
import re

def chuan_hoa_chuoi(s): 
    lines = s.splitlines()
    chuan_hoa_lines = []
    
    for line in lines:
        temp = line.strip()
        if temp:
            temp = re.sub(r'\s+', ' ', temp)
            temp = re.sub(r'\s+([.,])', r'\1', temp)
            temp = re.sub(r'([.,])(?=[^\s])', r'\1 ', temp) 
            chuan_hoa_lines.append(temp)           
    return "\n".join(chuan_hoa_lines)

chuoi_sach = chuan_hoa_chuoi(chuoi_chua_hoan_chinh)
print(chuoi_sach)