class Zwierz:
    def reply(self):    self.speak( )
    def glos(self):     print'spam'
class Ssak(Zwierz):
    def glos(self):     print'co?'
class Kot(Ssak):
    def glos(self):     print'mial'
class Pies(Ssak):
    def glos(self):     print'hau hau'
class SsakNaczelny(Ssak):
    def glos(self):     print'witaj'
class Haker(SsakNaczelny): pass
        