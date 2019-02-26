# Application de l'algorithme Apriori 
# Fait par Matthieu LOUF et Steve MAHOT 

# Définition des variables :

## Nombre d'occurences minimal
epsilon = 3

## Datasets (nombres ou mots): 
dataset_1 = [
    [1,2,5],
    [1,3,5],
    [1,2],
    [1,2,3,4,5],
    [1,2,4,5],
    [2,3,5],
    [1,5]
]

dataset_2 = [
    ["arbre", "orange", "thé", "banane"],
    ["carotte", "fruit", "orange", "banane", "thé"],
    ["carotte", "thé", "fruit"],
    ["arbre", "thé", "patate"],
    ["crevette", "fruit", "banane"],
    ["arbre", "banane", "thé", "orange", "crevette"],
    ["patate", "crevette", "thé", "banane", "arbre"],
    ["fruit", "thé", "banane", "crevette"]
]

# Définition des fonctions

# affiche les résultats contenu dans la liste "tab"
def afficher_resultat(list_Lk):
    for i in range(len(list_Lk)):
        if list_Lk[i] != [[],[]]:
            for j in range(len(list_Lk[i][0])):
                print(list_Lk[i][0][j])
            

def recherche_ind(tableau, nb):
    indice = 0
    for i in range(len(tableau)):
        if(tableau[i] == nb):
            indice = i
    return indice

# supprime les items identique dans une liste donnée
def remove_duplicate(d):
    return [i for n, i in enumerate(d) if i not in d[n + 1:]]

# renvoie Ck+1 à partir de Lk
def sous_ensembles (liste, k):
    res = list()
    if k == 2:
        for i in range (len(liste)):
            for j in range (i+1, len(liste)):
                res.append(list())
                res[len(res)-1].append(liste[i])
                res[len(res)-1].append(liste[j])
    else:
        for i in range (len(liste)):
            for j in range (i+1, len(liste)):
                res.append(list())
                res[len(res)-1].extend(liste[i])
                res[len(res)-1].extend(liste[j])
                res[len(res)-1] = remove_duplicate(res[len(res)-1])
                if len(res[len(res)-1]) != k:
                    del res[len(res)-1]

                if len(res) > 0:
                    res[len(res)-1].sort()
        res.sort()
        res = remove_duplicate(res)
    return res

# renvoie Ck avec le support
def calcul_occurences (set, liste):
    res = list()
    res.append(liste)
    res.append(list())
    for i in range (len(liste)):
        res[1].append(0)
        for j in range (len(set)):
            tot = 0
            for k in range (len(liste[i])):
                if liste[i][k] in set[j]:
                    tot += 1
            if tot == len(liste[i]):
                res[1][i] += 1
    return res

# supprime les ensembles dont l'occurence est inférieur à celui donné en paramètre
def elimination_ensembles(tab, min_occurences):
    tab_final = [[],[]]

    for i in range(len(tab[0])):
        if(tab[1][i]) >= min_occurences:
            tab_final[0].append(tab[0][i])
            tab_final[1].append(tab[1][i])
    
    return tab_final

# fonction principale de l'algorithme Apriori
def apriori(dataset, min_occurences): 
    # Calcul de C1
    C1 = [[],[]]
    for i in range(len(dataset)):
        for j in range(len(dataset[i])):
            if C1[0].count(dataset[i][j]) == 0:
                C1[0].append(dataset[i][j])
                C1[1].append(0)
            C1[1][recherche_ind(C1[0],dataset[i][j])] += 1
    
    # Calcul de L1
    Lk = [elimination_ensembles(C1,min_occurences)]

    k = 2
    Ck = C1

    # On peut commencer la boucle while principale
    # Elle s'arrête lorsque la fonction elimination_ensemble() ne renvoie rien
    while Lk[k-2] != [[],[]]:
        # Formation de tous les ensembles de taille k possibles à partir du Lk précédent
        ensembles_possibles_temp = sous_ensembles(Lk[k-2][0], k)

        # On rajoute un count à tous les ensembles possibles trouvés
        Ck = calcul_occurences(dataset, ensembles_possibles_temp)

        # On élimine les ensembles dont le nombre d'occurences est inférieur au paramètre
        L_k = elimination_ensembles(Ck,min_occurences)

        # On rajoute le groupe d'ensembles trouvés au tableau d'union des Lk
        Lk.append(L_k)
        k = k+1

    return Lk


# Execution de l'algorithme et affichage des résultats

print("\n Les sous-ensembles d'items fréquents avec un nombre d'occurrences > ", epsilon," :\n")
resultat = apriori(dataset_1, epsilon)
afficher_resultat(resultat)