import copy
print("Entrer la taille de votre matrice")
x=input()
l = x.split(" ",1)
ligne = int(l[0])
column = int(l[1])
a = [0] * ligne

for i in range(ligne):
    a[i] = [0] * column
"""
#Insertion dans notre matric A
for Lx in range(ligne):
    print("La colonne de gauche est utilisé pour définir le signe : 0:<= , 1:>= , 2:=0, 3: FO")
    print("Le résultat sera écrit toute a droite")
    print("Entrer la ligne "+ str(Lx) +" de votre matrice séparé par un espace")
    ligne1 = input()
    l1 = ligne1.split(" ", column )
    for i in range(column):
        a[Lx][i] = int(l1[i])
    print(a)
"""
a= [[7, 0, 1, 6], [1, 2, 0, 20], [0, 3, 4, 30], [-1, -2, -3, 0]]
#Def B 0
b = [0] * (ligne)
for i in range(ligne):
    b[i] = [0] * (column* 2)

#Remplir B avec A
for Lx in range(ligne):
    for i in range(column):
        if i == (column-1):
            b[Lx][i*2+1] = a[Lx][i] 
        else:
            b[Lx][i] =   a[Lx][i]
    b[Lx][Lx+column-1] = 1

#Y a t-il un négatif
isNegative = False
for i in range(column*2):
    if b[ligne-1][i] < 0 :
        isNegative = True
countWhile = 0
while(isNegative):
    #Find Pivot
    numberPivotColumn = 0
    for i in range(column*2-1):
        if b[ligne-1][i] <  numberPivotColumn :
            numberPivotColumn = b[ligne-1][i]
            indexPivotColumn = i
            
    if numberPivotColumn >= 0:
        isNegative = False
    numberLigneColumnPivot = []
    indexValueColumnToModify = []
    indexColumnToModify = []
    numberLigneColumnPivot = [9999] * (ligne)
    for i in range(ligne):
        numberLigneColumnAns = b[i][-1] #dernière valeure du tableau, donc le Ans
        print(" b[i][indexPivotColumn] " + str( b[i][indexPivotColumn]))
        if b[i][indexPivotColumn] > 0:
            numberLigneColumnPivot.insert(i,numberLigneColumnAns/b[i][indexPivotColumn])
            print("i " + str(i))
            

    numberLignePivot= numberLigneColumnPivot.index(min(numberLigneColumnPivot))
    print("Valeur du pivot " + str(numberLignePivot))
    print("Valeur du Number ligne Column " + str(numberLigneColumnPivot))
    for i in range(ligne):
        if b[i][indexPivotColumn] != 0 and i != numberLignePivot :
            indexValueColumnToModify.insert(i,b[i][indexPivotColumn])
            indexColumnToModify.insert(i,i)

    temp = copy.deepcopy(b)

            
    for i in range(ligne):
        for j in  range(column*2):
           
            if i in indexColumnToModify:
                # print("[i;j]: [" +str(i) + ";" + str(j)+"]")
                # print("first " +str(b[i][j])+ "   " +str(b[numberLignePivot][indexPivotColumn]) + "\t" + "sec " +str(b[numberLignePivot][j])+ "   " +str(b[i][indexPivotColumn]))
                # print("sec " +str(b[numberLignePivot][j])+ "   " +str(b[i][indexPivotColumn]))
                b[i][j] = temp[numberLignePivot][indexPivotColumn]*temp[i][j] - temp[i][indexPivotColumn]*temp[numberLignePivot][j]
                # print("result : " + str(b[i][j]))
    countWhile += 1
    print("nombre d'itération " + str(countWhile))
    print(b)
    #Find Pivot
    numberPivotColumn = 0
    for i in range(column*2-1):
        if b[ligne-1][i] <  numberPivotColumn :
            numberPivotColumn = b[ligne-1][i]
            indexPivotColumn = i
            
    if numberPivotColumn >= 0:
        isNegative = False
    print("-----------------------------------------------------------------------")
