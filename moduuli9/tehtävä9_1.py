class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, tamanhetkinennopeus, kuljettumatka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinennopeus = tamanhetkinennopeus
        self.kuljettumatka = kuljettumatka

#Pääohjelma
def main():
    auto = Auto("ABC-123", 142, 0, 0)
    print(f"Auton rekisteritunnus:{auto.rekisteritunnus} \nAuton huippunopeus:{auto.huippunopeus}km/h")
    return
main()