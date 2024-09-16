class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, tamanhetkinennopeus, kuljettumatka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinennopeus = tamanhetkinennopeus
        self.kuljettumatka = kuljettumatka
    def kiihdyta(self, nopeuden_muutos):
        if 0 < nopeuden_muutos + self.tamanhetkinennopeus < self.huippunopeus:
            self.tamanhetkinennopeus = self.tamanhetkinennopeus + nopeuden_muutos
        elif self.tamanhetkinennopeus + nopeuden_muutos < 0:
            self.tamanhetkinennopeus = 0
        else:
            self.tamanhetkinennopeus = self.huippunopeus
    def kulje(self, tunnit):
        self.kuljettumatka = tunnit * self.tamanhetkinennopeus

#Pääohjelma
def main():
    auto = Auto("ABC-123", 142, 0, 0)
    auto.kiihdyta(30)
    auto.kiihdyta(70)
    auto.kiihdyta(50)
    auto.kulje(2)
    print(f"Auton rekisteritunnus:{auto.rekisteritunnus} \nAuton huippunopeus:{auto.huippunopeus}km/h")
    print(f"Auton nopeus:{auto.tamanhetkinennopeus}")
    print(f"Auto on kulkenut {auto.kuljettumatka}km")
    return
main()