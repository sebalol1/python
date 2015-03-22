'''
Created on 1 mar 2015

@author: szielaskiewicz
'''
Liczba=100000
if Liczba ==1:
    print 0
elif Liczba == 2:
    print 1
else:
    f1=0L
    f2=1L
    n=Liczba-2
    while n>0:
        f2,f1, n=f1+f2,f2, n-1
    else:
        print f2
        print len(str(f2))