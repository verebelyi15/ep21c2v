class Kosar:
    def __init__(self):
        self.termekek = []
        self.termekek_darabszam = {}

    def append(self, termek):
        self.termekek.append(termek)

    def osszeg_lekerdezese(self) -> int:
        for termek in self.termekek:
            if termek not in self.termekek_darabszam:
                self.termekek_darabszam[termek] = 1
            else:
                self.termekek_darabszam[termek] += 1
        osszeg = 0
        for termek, darab in self.termekek_darabszam.items():
            if darab == 1:
                osszeg += 1000
            else:
                if osszeg == 2:
                    osszeg += 1900
                else:
                    if osszeg == 3:
                        osszeg += 2700
                    else:
                        osszeg += 2700 + (darab - 3) * 800
        return osszeg

    def termekek_lekerdezese(self) -> dict[str, int]:
        return self.termekek_darabszam

    def in_kosar(self, termek) -> bool:
        if termek in self.termekek_darabszam:
            return True
        return False