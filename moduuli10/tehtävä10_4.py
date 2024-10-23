import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, tamanhetkinennopeus, kuljettumatka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinennopeus = tamanhetkinennopeus
        self.kuljettumatka = kuljettumatka

    def kiihdyta(self, nopeuden_muutos):
        if 0 <= nopeuden_muutos + self.tamanhetkinennopeus <= self.huippunopeus:
            self.tamanhetkinennopeus = self.tamanhetkinennopeus + nopeuden_muutos
        elif self.tamanhetkinennopeus + nopeuden_muutos <= 0:
            self.tamanhetkinennopeus = 0
        else:
            self.tamanhetkinennopeus = self.huippunopeus

    def kulje(self, tunnit):
        self.kuljettumatka += tunnit * self.tamanhetkinennopeus

autot = []
a = 0
while True:
    if a < 10:
        autot.append(Auto(f"ABC-{a+1}", random.randint(100,200),0,0))
    else:
        break
    a += 1

class Kilpailu:
    def __init__(self, nimi, pituus, autot = []):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for i in range(len(autot)):
            autot[i].kiihdyta(random.randint(-10, 15))
            autot[i].kulje(1)

    def tilanne(self, tunnit):
        print(f'\ntunti {tunnit} tilanne:\n')
        for i in range(len(autot)):
            print(f"Rekisteri:{autot[i].rekisteritunnus}")
            print(f"Nopeus:{autot[i].tamanhetkinennopeus}")
            print(f"Kuljettumatka:{autot[i].kuljettumatka}")
            print("---------------------")
        for i in range(len(autot)):
            if autot[i].kuljettumatka > self.pituus:
                print(f"Auto {autot[i].rekisteritunnus} voitti")

    def kilpailu_ohi(self):
        for i in range(len(autot)):
            if autot[i].kuljettumatka > self.pituus:
                return True
        return False

#Pääohjelma (kilpailu)

def main():
    kilpailu = Kilpailu('Suuri romuralli', 8000, autot)
    loppu = False
    tunnit = 0
    while loppu == False:
        Kilpailu.tunti_kuluu(kilpailu)
        tunnit += 1
        if tunnit % 10 == 0:
            Kilpailu.tilanne(kilpailu, tunnit)
        loppu = Kilpailu.kilpailu_ohi(kilpailu)
    if loppu == True:
        Kilpailu.tilanne(kilpailu, tunnit)
    return
main()