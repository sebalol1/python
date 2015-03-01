a = b = []
b.append(1)
print a

a = []
b = []
b.append(1)
print a

a = [0]
b = [1, a]
a.append(b)
print a
print b