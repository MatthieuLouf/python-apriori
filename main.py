
def recherche_ind(tableau, nb):
    indice = 0
    for i in range(len(tableau)):
        if(tableau[i]==nb):
            indice =i
    return indice


def apriori(transactions, min_occurences):
    
    #Calcul de C1
    C1 =[[],[]]
    for i in range(len(transactions)):
        for j in range(len(transactions[i])):
            #print(transactions[i][j])
            if C1[0].count(transactions[i][j]) ==0:
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
        if C1[1][i]>= min_occurences:
            L_tab[0][0].append(C1[0][i])
            L_tab[0][1].append(C1[1][i])

    print("L1 : ")
    print(L_tab)

    k=2
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


#Tests :

"""
L = [2,4]
L.append([1,5,4,6])
print(L)
"""