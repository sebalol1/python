print "podaj liczbe"
liczba1 = int(raw_input())
jest = False
y = 1
while( y < liczba1) and not jest:
    if (y*y)==liczba1:
            jest=True
    y+=1
if jest:
    print 'tak'
else:
    print 'nie'