from pycsp3 import *
# import json
import sys
from itertools import product

data_file = sys.argv[1].replace("-data=",'')

stations = data.stations
regions= data.regions
interferences = data.interferences
liaisons = data.liaisons

nb_station = len(stations)
k = len(regions)

def domain_fe(i):
    return stations[i][3]
def domain_fr(i):
    return stations[i][4]

# -------- DONNEES FIXES -------------
# r[i] est le numéro de la région de la station i
r = []
# delta[i] est l'écart minimum entre deux fréquences de la station i
delta = []
# Delta[i] = [j, interf] où l'écart minimum entre les fréquences des stations i et j est interf
Delta  = []
for i in range(nb_station):
    r.append(stations[i][1])
    delta.append(stations[i][2])
    Delta.append([])

# n_i[i] est le nombre maximum de fréquences différentes utilisées pour la région i
n_i = []
for i in range(k):
    n_i.append(regions[i])

# Delta[i][j] =
for it in range(len(interferences)):
    for i in range(nb_station):
        if interferences[it][0] == i:
            Delta[i].append([interferences[it][1], interferences[it][2]])

# Les numéros des stations d'une même région
R = [[] for i in range(k)]
for i in range(nb_station):
    for j in range(k):
        if r[i] == j:
            R[j].append(2*i)
            R[j].append(2*i+1)
dom_R = [[] for i in range(k)]
for reg in range(k):
    for stat in R[reg]:
        if stat%2==0:
            i = int(stat/2)
            dom_R[reg].append(domain_fe(i))
            dom_R[reg].append(domain_fr(i))

# Renvoie la taille maximale des domaines et la liste de la taille de chaque domaine
# domain := indice pair représente les domaines des fe, indices impair représente les domaines de fr
# domain[2*i] := domaine de fe[i] et domain[2*i+1] := domaine de fr[i]
def max_size_domain_and_size_domain():
    max = -1
    size_domain = []
    domain = []
    for i in range(nb_station):
        domain.append(domain_fe(i))
        domain.append(domain_fr(i))
        dfe = len(domain_fe(i))
        dfr = len(domain_fr(i))
        size_domain.append(dfe) ; size_domain.append(dfr)
        if max < dfe:
            max = dfe
        if max < dfr:
            max = dfr
    return max, size_domain, domain


# Nombre de variable
n_var = 2*nb_station

# Nombre de fonction de coût # Nb de contraintes
n_cost_fct = nb_station + 4*len(interferences) + len(liaisons)

# Majorant initil
maj = 1000

max_size_domain, size_domain, domain = max_size_domain_and_size_domain()

# --- ECRITURE DU FORMAT WCSP


name_file = data_file.replace(".json",".wcsp")
format_wcsp = open(name_file, "w+")


# Première ligne : nom de l'instance nombre de variable taille maximale des domaines nombre de fonction de coût
format_wcsp.write(name_file+" "+str(n_var)+" "+str(max(size_domain))+" "+str(n_cost_fct)+" "+str(maj)+"\n")

# Deuxième ligne: taille de domaine de chaque variables
for i in range(len(domain)):
    format_wcsp.write(str(len(domain[i]))+" ")
format_wcsp.write("\n")

# Pour chaque fonctions de cout

#Contrainte d'écart entre deux fréquences d'une même stations (dure)
for stat in range(nb_station):
    fe_stat = domain_fe(stat)
    fr_stat = domain_fr(stat)
    nb_couple = 0
    for fei in range(len(fe_stat)):
        for fri in range(len(fr_stat)):
            if abs(fe_stat[fei] - fr_stat[fri]) == delta[stat]:
                nb_couple += 1
    # Arité de la fonction | numéro de vairables impliqué | Coût par défault | nombre de tuple listé après
    format_wcsp.write("2 "+str(2*stat)+" "+str(2*stat+1)+" "+str(maj)+" "+str(nb_couple)+"\n")
    for fei in range(len(fe_stat)):
        for fri in range(len(fr_stat)):
            if abs(fe_stat[fei] - fr_stat[fri]) == delta[stat]:
                # Tuple | coût associé
                format_wcsp.write(str(fei)+" "+str(fri)+" 0\n")

# Ecart minimum entre les fréquences de deux stations possèdant des interferences
for [stat1, stat2, Delta] in interferences:
    fe_s1 = domain_fe(stat1)
    fe_s2 = domain_fe(stat2)
    fr_s1 = domain_fr(stat1)
    fr_s2 = domain_fr(stat2)
    #Si les stations sont en liaisons on a une contrainte dure
    if [stat1, stat2] in liaisons:
        nb_couple = 0

        for fe1 in range(len(fe_s1)):
            for fe2 in range(len(fe_s2)):
                if abs(fe_s1[fe1] - fe_s2[fe2]) >= Delta :
                    nb_couple +=1
        # Arité de la fonction | numéro de vairables impliqué | Coût par défault | nombre de tuple listé après
        format_wcsp.write("2 "+str(2*stat1)+" "+str(2*stat2)+" "+str(maj)+" "+str(nb_couple)+" \n")
        for fe1 in range(len(fe_s1)):
            for fe2 in range(len(fe_s2)):
                if abs(fe_s1[fe1] - fe_s2[fe2])  >= Delta :
                    # Tuple | coût associé
                    format_wcsp.write(str(fe1)+" "+str(fe2)+" 0\n")

        nb_couple = 0
        for fe1 in range(len(fe_s1)):
            for fr2 in range(len(fr_s2)):
                if abs(fe_s1[fe1]-fr_s2[fr2]) >= Delta :
                    nb_couple +=1
        # Arité de la fonction | numéro de vairables impliqué | Coût par défault | nombre de tuple listé après
        format_wcsp.write("2 "+str(2*stat1)+" "+str(2*stat2+1)+" "+str(maj)+" "+str(nb_couple)+"\n")
        for fe1 in range(len(fe_s1)):
            for fr2 in range(len(fr_s2)):
                if abs(fe_s1[fe1]-fr_s2[fr2]) >= Delta :
                    # Tuple | coût associé
                    format_wcsp.write(str(fe1)+" "+str(fr2)+" 0\n")


        nb_couple = 0
        for fr1 in range(len(fr_s1)):
            for fe2 in range(len(fe_s2)):
                if abs(fr_s1[fr1]-fe_s2[fe2]) >= Delta :
                    nb_couple +=1
        # Arité de la fonction | numéro de vairables impliqué | Coût par défault | nombre de tuple listé après
        format_wcsp.write("2 "+str(2*stat1+1)+" "+str(2*stat2)+" "+str(maj)+" "+str(nb_couple)+"\n")
        for fr1 in range(len(fr_s1)):
            for fe2 in range(len(fe_s2)):
                if abs(fr_s1[fr1]-fe_s2[fe2]) >= Delta :
                    # Tuple | coût associé
                    format_wcsp.write(str(fr1)+" "+str(fe2)+" 0\n")

        nb_couple = 0
        for fr1 in range(len(fr_s1)):
            for fr2 in range(len(fr_s2)):
                if abs(fr_s1[fr1]-fr_s2[fr2]) >= Delta :
                    nb_couple +=1
        # Arité de la fonction | numéro de vairables impliqué | Coût par défault | nombre de tuple listé après
        format_wcsp.write("2 "+str(2*stat1+1)+" "+str(2*stat2+1)+" "+str(maj)+" "+str(nb_couple)+"\n")
        for fr1 in range(len(fr_s1)):
            for fr2 in range(len(fr_s2)):
                if abs(fr_s1[fr1]-fr_s2[fr2])  >= Delta :
                    # Tuple | coût associé
                    format_wcsp.write(str(fr1)+" "+str(fr2)+" 0\n")
    else:
        cost = 1 # Coup de la contrainte

        nb_couple = 0
        for fe1 in range(len(fe_s1)):
            for fe2 in range(len(fe_s2)):
                if abs(fe_s1[fe1] - fe_s2[fe2]) >= Delta :
                    nb_couple +=1
        # Arité de la fonction | numéro de vairables impliqué | Coût par défault | nombre de tuple listé après
        format_wcsp.write("2 "+str(2*stat1)+" "+str(2*stat2)+" "+str(cost)+" "+str(nb_couple)+" \n")
        for fe1 in range(len(fe_s1)):
            for fe2 in range(len(fe_s2)):
                if abs(fe_s1[fe1] - fe_s2[fe2]) >= Delta :
                    # Tuple | coût associé
                    format_wcsp.write(str(fe1)+" "+str(fe2)+" 0\n")

        nb_couple = 0
        for fe1 in range(len(fe_s1)):
            for fr2 in range(len(fr_s2)):
                if abs(fe_s1[fe1]-fr_s2[fr2]) >= Delta :
                    nb_couple += 1
        # Arité de la fonction | numéro de vairables impliqué | Coût par défault | nombre de tuple listé après
        format_wcsp.write("2 "+str(2*stat1)+" "+str(2*stat2+1)+" "+str(cost)+" "+str(nb_couple)+" \n")
        for fe1 in range(len(fe_s1)):
            for fr2 in range(len(fr_s2)):
                if abs(fe_s1[fe1]-fr_s2[fr2])  >= Delta :
                    # Tuple | coût associé
                    format_wcsp.write(str(fe1)+" "+str(fr2)+" 0\n")

        nb_couple = 0
        for fr1 in range(len(fr_s1)):
            for fe2 in range(len(fe_s2)):
                if abs(fr_s1[fr1]-fe_s2[fe2]) >= Delta :
                    nb_couple += 1
        # Arité de la fonction | numéro de vairables impliqué | Coût par défault | nombre de tuple listé après
        format_wcsp.write("2 "+str(2*stat1+1)+" "+str(2*stat2)+" "+str(cost)+" "+str(nb_couple)+" \n")
        for fr1 in range(len(fr_s1)):
            for fe2 in range(len(fe_s2)):
                if abs(fr_s1[fr1]-fe_s2[fe2]) >= Delta :
                    # Tuple | coût associé
                    format_wcsp.write(str(fr1)+" "+str(fe2)+" 0\n")

        nb_couple = 0
        for fr1 in range(len(fr_s1)):
            for fr2 in range(len(fr_s2)):
                if abs(fr_s1[fr1]-fr_s2[fr2]) >= Delta :
                    nb_couple += 1


        # Arité de la fonction | numéro de vairables impliqué | Coût par défault | nombre de tuple listé après
        format_wcsp.write("2 "+str(2*stat1+1)+" "+str(2*stat2+1)+" "+str(cost)+" "+str(nb_couple)+" \n")
        for fr1 in range(len(fr_s1)):
            for fr2 in range(len(fr_s2)):
                if abs(fr_s1[fr1]-fr_s2[fr2])  >= Delta :
                    # Tuple | coût associé
                    format_wcsp.write(str(fr1)+" "+str(fr2)+" 0\n")

# Condition pour les stations qui doivent communiquer
for [stat1, stat2] in liaisons:
    FE1 = domain_fe(stat1)
    FR1 = domain_fr(stat1)
    FE2 = domain_fe(stat2)
    FR2 = domain_fr(stat2)

    nb_couple = 0
    for fe1 in range(len(FE1)):
        for fr1 in range(len(FR1)):
            for fe2 in range(len(FE2)):
                for fr2 in range(len(FR2)):
                    if FE1[fe1] == FR2[fr2] and FR1[fr1] == FE2[fe2]:
                        nb_couple += 1
    # Arité de la fonction | numéro de vairables impliqué | Coût par défault | nombre de tuple listé après
    format_wcsp.write("4 "+str(2*stat1)+" "+str(2*stat1+1)+" "+str(2*stat2)+" "+str(2*stat2+1)+" "+str(maj)+" "+str(nb_couple)+"\n")

    for fe1 in range(len(FE1)):
        for fr1 in range(len(FR1)):
            for fe2 in range(len(FE2)):
                for fr2 in range(len(FR2)):
                    if FE1[fe1] == FR2[fr2] and FR1[fr1] == FE2[fe2]:
                        # Tuple | coût associé
                        format_wcsp.write(str(fe1)+" "+str(fr1)+" "+str(fr2)+" "+str(fe2)+" 0\n")



format_wcsp.close()
