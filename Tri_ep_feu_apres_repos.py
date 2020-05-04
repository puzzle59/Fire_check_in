import sys 

#print(sys.argv)
#args given in a shell are saved as a list, which 1st element is module's name
list_shell=[]
for item in sys.argv[1:]:
    list_shell.append(int(item))
biggest=0   
transitive_var=0

#def tri(list_shell,up_or_done):
#up_or_done='>' bonus, obtenir le croissant si desiré 
for current_item_index in range(len(list_shell)-1):
    biggest=list_shell[current_item_index]
    biggest_index=current_item_index

#la boucle s'arrête à l'avant dernier := ))    
    for remaining_item_index in range(current_item_index+1,len(list_shell)):
#ok donne le bon index pour la deuxieme boucle print(list_shell[remaining_item_index])
        if list_shell[remaining_item_index]> biggest:
            biggest=list_shell[remaining_item_index]
            biggest_index=remaining_item_index
#        FAIRE LE SWITCH ENTRE BIGGEST ET CURRENT
    transitive_var=list_shell[current_item_index]
    list_shell[current_item_index]=biggest  
    list_shell[biggest_index]=transitive_var

print(list_shell)    