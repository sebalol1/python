# proste definicje klas

class NicNieRob:
    pass

dir(NicNieRob)

# przykladowa klasa bez inicjalizacji

class MyClass:
    "A simple example class"
    i = 12345
    def f(self):
        return 'hello world'

x = MyClass()
x.f()
print x.i
print x.__doc__
print '-'*20

# klasa z inicjalizacja stanu klasy

class MojaKlasa:
    i = 1
    def __init__(self, a = 10, b = 20):
        self.__class__.i += 1
        self.a = a
        self.b = b
    def wypisz(self):
        print self.i, self.a, self.b,

y = MojaKlasa(30,40)
y.wypisz()
z = MojaKlasa()
z.wypisz()
MojaKlasa(13).wypisz()

# czym jest
MojaKlasa.wypisz
# a czym
y.wypisz

# z drugiej strony
y.wypisz()
# jest rownowazne
MojaKlasa.wypisz(y)


# kasujemy atrybuty obiektu
#del y.i
#del y.a
#print y.a

# a teraz klasy
#del MojaKlasa.i
# metody tez mozemy kasowac
#del MojaKlasa.wypisz
# ale czy z obiektu tez mozna usuwac metody?

    