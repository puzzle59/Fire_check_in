import sys 
sentence= sys.argv [1]

s_updated=""
indicateur=0

for i in range(len(sentence)):
    if sentence[i]!=(" "):
        if indicateur==0: 
            s_updated+=sentence[i].lower()
            indicateur=1
            continue
        if indicateur==1:
            s_updated+=sentence[i].upper()
            indicateur=0 
    else:
        s_updated+=sentence[i]
        

    
#Amélioration possible: à l'image de " " , prendre en compte , ; ? ! . - etc
#pour que deux lettres consécutives soit tj comme proposé , même si c'est plus qu'une phrase.

#je considère cet exo terminé pour le moment,je continue d'avancer s
print(s_updated)
        
        
        
        
        
   
    
       