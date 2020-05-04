from sys import argv 
script, compared_word, file1 = argv 
long_compared_word=len(compared_word)
words_list=[]
f=open(file1, 'r')
for line in f:
    words_list.append(line)
# attention, l'antislah n revient à la charge ..
print(words_list)
print(long_compared_word)
m=[]
for item in words_list:
    if len(item)==long_compared_word+1 :
        m.append(item[:long_compared_word])
print("voici la liste rabotée %s" %m)        

def decortik(word):
    youhou=[]
    for u in word:
        youhou.append(u)
    return youhou    
"""the decortik function takes a word in argument and return caracteres of 
this word into a list. it separate the letters :==) """

def is_it_anagram(w1,w2):
    
    h=decortik(w1)
    k=decortik(w2)
    for jiji in h:
         if jiji in k:
           k.remove(jiji)
           
    if k==[]:
        return True 
    else: 
        return False 
for item in m:
    if is_it_anagram(compared_word,item):
        print(item)
        