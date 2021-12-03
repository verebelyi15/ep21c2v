from pathlib import Path
from kosar import Kosar
from datetime import datetime


class Bolt: ...


class App(Bolt):
    def __init__(self):
        self.kosarak = []
        self.all_of_termek_type = set()

    def feladat_1(self, filepath: Path) -> None:
        if filepath.exists():
            with open(filepath) as file:
                sorok = file.readlines()

                kosar = None
                for sor in sorok:
                    sor = sor.strip()
                    if kosar == None:
                        kosar = Kosar()
                    elif sor == "F":
                        self.kosarak.append(kosar)
                        kosar = Kosar()
                    if sor != "F":
                        kosar.append(sor)

            for kosar in self.kosarak:
                for termek in kosar.termekek:
                    self.all_of_termek_type.add(str(termek))

    def feladat_2(self) -> None:
        print("Ennyien fizettek a pénztárnál: ", len(self.kosarak))

    def sorszaminput(self) -> int:
        print("Kérem a sorszámot: ")
        sorszam = input()
        try:
            sorszam = int(sorszam)
        except:
            pass

        if type(sorszam) == int:
            return int(sorszam)
        else:
            print("Hibás sorszám")
            return self.sorszaminput()

    def feladat_3(self) -> None:
        sorszam = self.sorszaminput()
        print("Összesen:", len(self.kosarak[sorszam].termekek), "darab")
        print("Összesen fizetendő összeg:", self.kosarak[sorszam].osszeg_lekerdezese())
        print("Termékek a kosárban:")
        for termek, darab in self.kosarak[sorszam].termekek_lekerdezese().items():
            print("\t", termek, darab, "db")

    def arucikk_bekeres(self) -> str:
        print("Kerem ijron be egy arucikket:")
        arucikk = input()
        if arucikk not in self.all_of_termek_type:
            print("Hibas arucikk kerem irjon be ujat az alabiiak kozul:")
            for termek in self.all_of_termek_type:
                print("\t", termek, end="")
            print()
            return self.arucikk_bekeres()
        else:
            return arucikk

    def feladat_4(self) -> None:
        arucikk = self.arucikk_bekeres()
        summmmma = 0
        for kosar in self.kosarak:
            for termek in kosar.termekek:
                if termek == arucikk:
                    summmmma += 1
        print("Ennyi db van osszesen a kosarakban a ", arucikk, "-bol:", summmmma, "db")

    def feladat_5(self, filepath: Path) -> None:
        stringem = "Kiírás megtörtént: " + str(datetime.now().isoformat()) + " -kor \n"
        for idx, kosar in enumerate(self.kosarak):
            stringem += str(idx + 1) + ". Kosár: " + str(kosar.osszeg_lekerdezese()) + " HUF \n"
        if filepath.exists():
            with open(filepath, "a") as file:
                file.write("\n" + stringem)
        else:
            with open(filepath, "w") as file:
                file.write(stringem)

    def run(self):
        self.feladat_1(Path("kosar.txt"))
        self.feladat_2()
        self.feladat_3()
        self.feladat_4()
        self.feladat_5(Path("kosar_kiiras.txt"))


if __name__ == '__main__':
    app = App()
    app.run()