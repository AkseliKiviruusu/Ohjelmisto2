class Hissi:
    def __init__ (self, alin, ylin, kerros = 0):
        self.kerros = kerros
        self.alin = alin
        self.ylin = ylin

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
            print(f"Hissi on nyt kerroksessa:\n{hissi.kerros}")
        else:
            print("Kerrosta ei ole olemassa.")

# pääohjelma
hissi = Hissi(alin = -1, ylin = 20)
hissi.siirry(12)
hissi.siirry(hissi.alin)