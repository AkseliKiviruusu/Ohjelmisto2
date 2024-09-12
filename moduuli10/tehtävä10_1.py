class Hissi:
    def __init__ (self, alin, ylin, kerros = 0):
        self.kerros = kerros
        self.alin = alin
        self.ylin = ylin

    def alas(self):
        self.kerros -= 1

    def ylos(self):
        self.kerros += 1

    def siirry(self, kerrokseen):
        if self.alin <= kerrokseen <= self.ylin:
            while kerrokseen < self.kerros:
                self.alas()
            while kerrokseen > self.kerros:
                self.ylos()
            print(f"Hissi on nyt kerroksessa:\n{hissi.kerros}")
        else:
            print("Kerrosta ei ole olemassa.")

# pääohjelma
hissi = Hissi(alin = -1, ylin = 20)
hissi.siirry(12)
hissi.siirry(hissi.alin)