def slownie(liczba):
    cyfry=['zero','jeden','dwa','trzy','cztery','piec','szesc','siedem','osiem','dziewiec']
    return map(lambda x:cyfry[int(x)],str(liczba))
print slownie(18934) 

a=1111
print a, hex(a), oct(a), bin(a)