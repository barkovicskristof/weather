# név: Barkovics Kristóf

class Szemely:
    def __init__(self, vez_nev, ker_nev):
        self.vez_nev = vez_nev
        self.ker_nev = ker_nev

    def __str__(self):
        return f"{self.vez_nev} {self.ker_nev}"


class Tanar(Szemely):
    def __init__(self, vez_nev, ker_nev, kod, *szakok):
        super().__init__(vez_nev, ker_nev)
        self.kod = kod
        self.szakok = szakok

    def __str__(self):
        return f"{self.vez_nev} {self.ker_nev} ({self.kod}) : {', '.join(self.szakok)}"


class Diak(Szemely):
    def __init__(self, vez_nev, ker_nev, osztaly, tantargy):
        super().__init__(vez_nev, ker_nev)
        self.osztaly = osztaly
        self.tantargy = tantargy

    def __str__(self):
        return f"{self.vez_nev} {self.ker_nev}, {self.osztaly} : {self.tantargy}"


def adatok_beolvasasa(file_path):
    tanarok = []
    diakok = []

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            data = line.strip().split(';')
            if data[0] == 'T':
                tanarok.append(Tanar(data[1], data[2], data[3], *data[4:]))
            elif data[0] == 'D':
                diakok.append(Diak(data[1], data[2], data[3], data[4:]))

    return tanarok, diakok, len(tanarok), len(diakok)
