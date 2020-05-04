import sys 
script, in_file=sys.argv
f=open(in_file, 'r')
#ligne mesure 11 +1 pur \n , sauf la dernière du coup 
#colonne mesure... 11 également, +0 car pas de  \n cette fois 
matrice=[]
for line in f.readlines():
    u=[]
    for char in line:
        if (char!=("|") and char!= "\n" and char!="+" and char!="-"):
            u.append(char)
    matrice.append(u)
f.close()

for j in matrice:
   if len(j)==0:
    matrice.remove(j)
#Rabotage de matrice pour n'avoir que les 9 listes nécessaires et pas de +++
#print("voici les 9 listes épurèes %s" %matrice)

def where_hole(list):
    """trouve la position de "_" dans la liste avec info lignes 
    """
    ainsi_soit_il=[]
    compteur=0
    for item in list :
        if item== "_":
            ainsi_soit_il.append(compteur)
        compteur+=1
    return ainsi_soit_il

    
def holes_number(liste ):
    return len(where_hole(liste))

def whats_missing(sudoku_list):
    full_list=[1,2,3,4,5,6,7,8,9]
    for item in sudoku_list:
        if item!='_':
            item=int(item)
        
        if item in full_list:
            full_list.remove(item)
    return full_list

for line in matrice:
    if holes_number(line)<=1 and holes_number(line)>0 :
        line[where_hole(line)[0]]=whats_missing(line)[0]

def colonne(matrice,numero):
    colonne=[]
    for item in matrice:
        colonne.append(item[numero])
    return colonne 
#ok fonctionnel 
U=[]
for u in range(9):
    U.append(colonne(matrice,u))
    
for column in U:
    if holes_number(column)<=1 and holes_number(column)>0 :
        column[where_hole(column)[0]]=whats_missing(column)[0]
matrice_bis=[]
for f in range(9):
    for u in U:
        matrice_bis.append(u[f])
#sudoku fini, de ligne en ligne, 81 caractères dans une seule liste

alpha=("%s" %matrice_bis[:9])+"\n"+("%s" %matrice_bis[9:18])
alpha+="\n" +("%s" %matrice_bis[18:27])+"\n"+ ("%s" %matrice_bis[27:36])+ "\n"
alpha+=("%s" %matrice_bis[36:45])+"\n"+ ("%s" %matrice_bis[45:54])+ "\n"
alpha+=("%s" %matrice_bis[54:63])+"\n"+ ("%s" %matrice_bis[63:72])+ "\n"
alpha+=("%s" %matrice_bis[72:81])+"\n"+ "AHhahahahahahahahhah :) ) :) good job"

print(alpha)


# #Colonnes maintenant :
# g=open(in_file,'r')
# columns=[]
# for j in range(11):
#     colonne=[]
#     while len(colonne)!=9:
#         g.seek(j)
#         item=g.read(1)
#         if item!="-":
#             colonne.append(item)
#         j+=12    
#     columns.append(colonne)
# g.close()
# columns.remove(columns[3])
# columns.remove(columns[6])
#colonnes "vierges"
#ok. acces aux 9 colonnes 
        
#ok trouve le chiffre manquant !
# def ou_est_charlie (matrice):
#     g=open(in_file,'r')
#     stockons_le_resultat=[]
#     i=0
#     for elements in matrice:
#         if holes_number(elements) <=1:
#             stockons_le_resultat+=[whats_missing(elements),i]
#         else:
#             print(whats_missing(recup_collone(g,where_hole(elements))))
#         i+=1    
#     return  stockons_le_resultat
# print(ou_est_charlie(matrice))
