a = "abcdef"
b = a[0:1000]

# 주소가 동일
print(id(a))
print(id(b))