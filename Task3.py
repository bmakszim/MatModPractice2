import os

import numpy as np
import requests

# EZT kell módosítani
# file webes elérési útja 
file_url = "http://cs.joensuu.fi/sipu/datasets/dim032.txt"
# letöltött fájl neve
file_name = "dim032.txt"

# NEM kell megváltoztatni
# a mappa, ahová letöltünk
data_folder = "data"
os.makedirs(data_folder, exist_ok=True)
# adatfájl teljes elérési útja
data_file = os.path.join(data_folder, file_name)
# internetről letöltés
r = requests.get(file_url, allow_redirects=True)
open(data_file, "wb").write(r.content)
# letöltött fájl beolvasása
# a betöltött adatot a `data` nevű változóban tároljuk
data = np.loadtxt(data_file)

p = data[100]
counter = 0

for q in data:
    dist = np.max(np.abs(p - q))
    if (dist < 35):
        counter += 1

print(counter - 1) # -1, mert az egyik onmaga