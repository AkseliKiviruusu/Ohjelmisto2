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

class Sahko(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, tamanhetkinennopeus, kuljettumatka, akku_kwh):
        super().__init__(rekisteritunnus, huippunopeus, tamanhetkinennopeus, kuljettumatka)
        self.akku_kwh = akku_kwh

class Poltto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, tamanhetkinennopeus, kuljettumatka, tankki):
        super().__init__(rekisteritunnus, huippunopeus, tamanhetkinennopeus, kuljettumatka)
        self.tankki = tankki

# Pääohjelma:
def main():

    sahkoauto = Sahko('ABC-15', 180, 80, 0, 52.5)
    poltto = Poltto('ACD-123', 165, 100, 0, 32.3)

    sahkoauto.kulje(3)
    poltto.kulje(3)

    print(f'kuljettumatka: {sahkoauto.kuljettumatka}')
    print(f'kuljettumatka: {poltto.kuljettumatka}')
    return

main()