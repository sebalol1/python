print "!!!!UWAGA!!!!"
print "PAMIETAJ, ZEBY B>A"
#print "podaj liczbe a"
#a=int(raw_input())
#print "podaj liczbe b"
#b=int(raw_input())
def euklides(a,b):
    while a !=b:
        if a>b:
            a -=b
        else:
            b -= a
    return a

print euklides (160,120)
def euklides2(*args):
    return reduce(euklides, args)
lista=[16,4,8]
print euklides2(10,15,5,100,30,60,20,80,5,5,3265,10,320,230,3540,325,320,325)



        
    