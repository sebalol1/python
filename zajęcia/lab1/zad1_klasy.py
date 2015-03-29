class Sum:
    def dodaj(self,x,y):
        print "brak implementacji"
    def __init__(self,start=[ ]):
        self.data=start
    def __dodaj__(self,other):
        return self.dodaj(self.data,other)
    
    
    
class ListaSum(Sum):
    def dodaj(self, x, y):
        return x+y
    
class SlowSum(Sum):
    def dodaj(self, x, y):
        new= {  }
        for k in x.keys( ):new[k]=x[k]
        for k in y.keys( ):new[k]=y[k]
        return new