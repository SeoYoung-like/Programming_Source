a = [10, 20, 30]
print(a[len(a):])

a[len(a):] = 500
print(f"a[len(a):] - id:{str(id(a)):15}  value:{str(a):5}")
a.append(600)
print(f"a.appen(a) - id:{str(id(a)):15}  value:{str(a):5}")