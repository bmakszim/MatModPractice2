import os
import numpy as np
import requests

def read_data(url):
    # file webes elérési útja 
    file_url = url
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
    return np.loadtxt(data_file)

def count_within_distance(data, p, distance):
    counter = 0
    for q in data:
        dist = np.max(np.abs(p - q))
        if (dist < distance):
            counter += 1

    return counter - 1 # 1 onmaga

data = read_data("http://cs.joensuu.fi/sipu/datasets/dim032.txt")
result = count_within_distance(data, data[50], 150)

print(result) # -1, mert az egyik onmaga