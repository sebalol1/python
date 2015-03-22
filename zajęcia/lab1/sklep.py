lista={'a':1,"b":2,'c':3}

def zakupy2(l,*x):
    return reduce((lambda x, y:x+y), [l[k] for k in x])
aaa=['a','b','c']
print zakupy2(lista, *aaa)



