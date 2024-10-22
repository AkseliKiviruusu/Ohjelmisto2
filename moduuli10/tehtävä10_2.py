class Hissi:
    def __init__ (self, alin, ylin, id, kerros = 0):
        self.kerros = kerros
        self.alin = alin
        self.ylin = ylin
        self.id = id

    def alas(self):
        self.kerros -= 1

    def ylos(self):
        self.kerros += 1

    def siirry(self, uusi_kerros):
        if self.alin <= uusi_kerros <= self.ylin:
            while uusi_kerros < self.kerros:
                self.alas()
            while uusi_kerros > self.kerros:
                self.ylos()
            print(f"Hissi {self.id-1} on nyt kerroksessa:\n{self.kerros}")
        else:
            print("Kerrosta ei ole olemassa.")

class Talo:
    def __init__ (self, alin, ylin, hissit_lkm):
        self.alin = alin
        self.ylin = ylin
        self.hissit_lkm = hissit_lkm
        self.hissit = []

    def create_hissit(self):
        for i in range(self.hissit_lkm):
            hissi = Hissi(self.alin, self.ylin, i+1)
            self.hissit.append(hissi)

    def move_hissi(self, hissi_index, kerros):
        if 0 <= hissi_index < len(self.hissit):
            self.hissit[hissi_index].siirry(kerros)

#Pääohjelma

def main():
    talo = Talo(0, 20, 3)
    talo.create_hissit()
    talo.move_hissi(1,20)
    talo.move_hissi(2,15)
    return
main()