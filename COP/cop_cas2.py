from pycsp3 import *
import sys


stations = data.stations
regions= data.regions
interferences = data.interferences
liaisons = data.liaisons

n = len(stations) # nombre de station
k = len(regions) # nombre de région
int = len(interferences) # nombre d'interferences

print(n," stations et ",k," régions")

def domain_fe(i):
    return stations[i][3]
def domain_fr(i):
    return stations[i][4]

# fe[i] la fréquence émettrice de la station i
fe = VarArray(size=n, dom=domain_fe)
# fr[i] la fréquence réceptrice de la station i
fr = VarArray(size=n, dom=domain_fr)


# -------- DONNEES FIXES -------------
# r[i] est le numéro de la région de la station i
r = []
# delta[i] est l'écart minimum entre deux fréquences de la station i
delta = []
# Delta[i] = [j, interf] où l'écart minimum entre les fréquences des stations i et j est interf
Delta  = []
for i in range(n):
    r.append(stations[i][1])
    delta.append(stations[i][2])
    Delta.append([])

# n_i[i] est le nombre maximum de fréquences différentes utilisées pour la région i
n_i = []
for i in range(k):
    n_i.append(regions[i])

# Delta[i][j] =
for it in range(len(interferences)):
    for i in range(n):
        if interferences[it][0] == i:
            Delta[i].append([interferences[it][1], interferences[it][2]])

# Les variables d'une même région
R = [[] for i in range(k)]
for i in range(n):
    for j in range(k):
        if r[i] == j:
            R[j].append(fe[i])
            R[j].append(fr[i])

# Les contraintes
satisfy (
    # Ecart minimum entre les fréquences d'une même station
    [abs(fe[i] - fr[i]) == delta[i] for i in range(n)],

    # Contraintes de fréquences pour les interférences
    [abs(fe[i] - fe[Delta[i][j][0]]) >= Delta[i][j][1] for i in range(n) for j in range(len(Delta[i]))],

    [abs(fe[i] - fr[Delta[i][j][0]]) >= Delta[i][j][1] for i in range(n) for j in range(len(Delta[i]))],

    [abs(fr[i] - fe[Delta[i][j][0]]) >= Delta[i][j][1] for i in range(n) for j in range(len(Delta[i]))],

    [abs(fr[i] - fr[Delta[i][j][0]]) >= Delta[i][j][1] for i in range(n) for j in range(len(Delta[i]))],

    # Le nombre de féquence différentes pour une même région j est au maximum n_i[i]
    [NValues(R[i]) <= n_i[i] for i in range(k)],

    # Contrainte de liaison
    [(fe[i] == fr[j]) & (fr[i] == fe[j]) for [i,j] in liaisons]
)


# La fonction objective
minimize(
    Sum(fe+fr)
)

#Si c'est satisfiable, on imprime la solution
if solve() is OPTIMUM:
    FE = values(fe)
    FR = values(fr)
    for i in range(len(fe)):
        print("Station ",i," fe ",FE[i]," fr ",FR[i])
    print("Fréquence la plus hautes",max(set(FE+FR)))
