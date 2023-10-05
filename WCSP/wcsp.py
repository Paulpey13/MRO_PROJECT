import json
import sys

data_file = sys.argv[1]

with open(data_file) as file:
    data = json.load(file)



stations = data["stations"]
regions= data["regions"]
interferences = data["interferences"]
liaisons = data["liaisons"]

# Nombre de variable
n_var = 2*len(stations)

def domain_fe(i):
    return stations[i][3]
def domain_fr(i):
    return stations[i][4]

# Renvoie la taille maximale des domaines et la liste de la taille de chaque domaine
def max_size_domain_and_size_domain():
    max = -1
    size_domain = []
    for i in range(n_var):
        dfe = len(domain_fe(i))
        dfr = len(domain_fr(i))
        size_domain.append(dfe) ; size_domain.append(dfr)
        if max < dfe:
            max = dfe
        if max < dfr:
            max = dfr
    return max, size_domain



max_size_domain, size_domain = max_size_domain_and_size_domain()

# --- ECRITURE DU FORMAT WCSP

name_file = "wcsp_"+data_file
format_wcsp = open(name_file, "w+")

# Première ligne : nom de l'instance nombre de variable taille maximale des domaines nombre de fonction de coût
...

# Deuxième ligne: taille de chaque domaine
...

# Pour chaque contrainte
