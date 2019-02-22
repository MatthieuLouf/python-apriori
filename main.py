
def recherche_ind(tableau, nb):
    indice = 0
    for i in range(len(tableau)):
        if(tableau[i]==nb):
            indice =i
    return indice

def remove_duplicate(d):
    return [i for n, i in enumerate(d) if i not in d[n + 1:]]

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

                res[len(res)-1].sort()
        res.sort()
        res = remove_duplicate(res)
    return res

#renvoie Cn avec le sup : fait le scan D
def calcule_occurences (set, liste):
    res = list()
    res.append(liste)
    res.append(list())
    for i in range (len(liste)):
        res[1].append(0)
        for j in range (len(set)):
            tot = 0
            for k in range (len(liste[i])):
                if liste[i][k] in set[j]:
                    tot+=1
            if tot == len(liste[i]):
                res[1][i] += 1
    return res


def apriori(transactions, min_occurences):  
    
    #Calcul de C1
    C1 =[[],[]]
    for i in range(len(transactions)):
        for j in range(len(transactions[i])):
            #print(transactions[i][j])
            if C1[0].count(transactions[i][j]) == 0:
                C1[0].append(transactions[i][j])
                C1[1].append(0)
            C1[1][recherche_ind(C1[0],transactions[i][j])] +=1
    
    print("C1 : ")
    print(C1)
    
    #Calcul de L1
    L_tab = [
        [[],[]] #premier indice gère les Lk puis les deux autres item_set et le support
        ] 
    for i in range(len(C1[0])):
        if C1[1][i] >= min_occurences:
            L_tab[0][0].append(C1[0][i])
            L_tab[0][1].append(C1[1][i])

    print("L1 : ")
    print(L_tab)

    k=2 #itération
    C_tab=C1

    #On peut commencer la boucle while principale


    #return L_tab

transactions_set = [
    [1,2,5],
    [1,3,5],
    [1,2],
    [1,2,3,4,5],
    [1,2,4,5],
    [2,3,5],
    [1,5]
]

epsilon = 3
print(apriori(transactions_set,epsilon))


#Tests unitaires & cie:

print("Test")
L1 = [1,2,3]
L2 = [[1,2], [1,3], [1,5], [2,3], [2,5], [3,5]]

print(len(L1))
print(len(L2))
print(len(L2[0]))

print("\nsous_ensembles :")
res1 = sous_ensembles(L1, 2)
res2 = sous_ensembles(L2, 3)
print(res1)
print(res2)

print("\noccur :")
print(calcule_occurences(transactions_set, res1))
print(calcule_occurences(transactions_set, res2))

print("\nL1, L2 :")
print(L1)
print(L2)

