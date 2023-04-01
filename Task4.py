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

p = data[70]
q = data[250]

def calc_angle(u, v):
    numerator = np.sum(u * v)
    u_abs = np.sqrt(np.sum(u ** 2))
    v_abs = np.sqrt(np.sum(v ** 2))
    denominator = u_abs * v_abs
    return np.arccos(numerator / denominator)

result = calc_angle(p, q)

print(result)