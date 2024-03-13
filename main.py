# név: Barkovics Kristóf

from model import adatok_beolvasasa

tanarok, diakok, tanarok_szama, diakok_szama = adatok_beolvasasa('személyek.txt')

print("Tanárok száma:", tanarok_szama)
for tanar in tanarok:
    print("\t", tanar)

print("\nDiákok száma:", diakok_szama)
for diak in diakok:
    print("\t", diak)
