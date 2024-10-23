class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(self.nimi)

class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        self.paatoimittaja = paatoimittaja
        super().__init__(nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(self.paatoimittaja)

class Kirja(Julkaisu):
    def __init__(self,nimi, kirjoittaja, sivumaara):
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara
        super().__init__(nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(self.kirjoittaja)
        print(self.sivumaara)

def main():
    julkaisu = Kirja('Harry Potter', 'J.K. Rowling', 459)
    julkaisu2 = Lehti('Suomen Kuvalehti','Matti Kalliokoski')
    julkaisu.tulosta_tiedot()
    print()
    julkaisu2.tulosta_tiedot()
    return
main()