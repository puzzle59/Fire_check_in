import sys 
script, file1 , file2 = sys.argv

l=[]
f=open(file1,"r")
for line in f:
    l.append(line)

long_c1=len(l[0])-1
#largeur du rectangle ok
#creation liste de c1 sans les \n pour pouvoir comparer avec l_comp

m=[]
for items in l:
    if len(items)>=long_c1:
        
        m.append(items[:long_c1])
    else:
        m.append(items)
f.close()



f=open(file2, "r")
first_line=f.readline()
long_c2=len(first_line)



def function(compteur):
    l_comp="124"

    while (l_comp != m[0]):
        l_comp=f.read(long_c1)
        f.seek(compteur)
        compteur+=1
    compteur+=(-2)    
    saved_position=compteur
    compteur+= long_c2
    f.seek(compteur)
    discovered_lines=1
    for item in m[1:]:
        if f.read(long_c1) == item :
            compteur+=long_c2
            f.seek(compteur)
#            discovered_lines+=1
#            print(discovered_lines)
        else:
            
            return function(saved_position+1)
    
    return (saved_position%long_c2,saved_position//long_c2)

print(function(1))



# if (f.read(3)== m[1]):
#     print("c'est déjà ça poto %s" )
#     compteur+=long_c2
#     f.seek(compteur)
    
#     print(" youhou %d" %f.tell())
#     if f.read(3)==m[2]:


f.close()


#comment coupler le tout pour n'importe quel carrée ???     

#ok code trouve la premiere ligne de c1 dans c2
#trouve la deuxieme ; la troisieme ; BONNE persévérance c'est bien!!!!


#besoin d'un compteur, retour en arrière via seek , incontournable
#sous forme de liste à 2elmts [x,y]
#OU SIMPLEMENT récup position via %% et // ;) 
#f.read(nbre) reçoit le caractère puis avance.
#besoin de progresser pas à pas car le curseur se déplace après le read 
#on ne voudrait pas louper le début de la 1ere ligne de c1.txt..



""" POUR LE 21 AVRIL 2020 BOULOT EN SOIREE 
Restera à automatiser: les longueurs , le nombre de lignes, while<for<while 
pour aller chercher tout ce qu'il faut, et retourner où on en était si 1ere lig
ne ok mais deuxieme non, etc , jusqu'a à avoir trouver toutes les lignes et 
afficher la position sauvegardée au moment où on trouve la premiere ligne 
Me suis fait avoir par les \n reçu depuis le fichier , du coup les strings 
étaient identiques mais de longueurs différentes, ça renvoyait donc False ...

Bon travai! Bien avancé! Avec les string formattés notamment(pas de " , " 
entre texte
et variables..) bien manipuler les fichiers 

il restera également à régler le problème du fichier en argument qui n'est 
pas lu par open pour l'instant. Good night .. à demain matin ;) 


ET de un !!! Plus que 3 ;) 
"""

