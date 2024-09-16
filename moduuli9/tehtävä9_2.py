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

#Pääohjelma
def main():
    auto = Auto("ABC-123", 142, 0, 0)
    print(f"Auton rekisteritunnus:{auto.rekisteritunnus} \nAuton huippunopeus:{auto.huippunopeus}km/h")
    auto.kiihdyta(30)
    auto.kiihdyta(70)
    auto.kiihdyta(50)
    print(f"Auton nopeus:{auto.tamanhetkinennopeus}")
    auto.kiihdyta(-200)
    print(f"Auton nopeus:{auto.tamanhetkinennopeus}")
    return
main()