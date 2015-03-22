from cmath import sqrt
x=0
y=0
a=int(raw_input("Podaj liczbe a "))
b=int(raw_input("Podaj liczbe b "))
c=int(raw_input("Podaj liczbe c "))
delta=b*b-4*a*c
print "delta wynosi:"
print delta
if delta<0:
    print "brak rozwiazan"
elif delta == 0:
    print "rownanie ma jedno rozwiazanie"
    x=-b/2*a
else:
    print "rownanie ma dwa rozwiazania"
    x=(-b+sqrt(delta))/2*a
    y=(-b-sqrt(delta))/2*a
print x
print y      
print "------------------------------------------"        

dd=sqrt(-delta)*1j
if delta<0:
    print "brak rozwiazan"
elif delta == 0:
    print "rownanie ma jedno rozwiazanie"
    x=-b/2*a
else:
    print "rownanie ma dwa rozwiazania"
    x=(-b+dd)/2*a
    y=(-b-dd)/2*a
print x
print y 
