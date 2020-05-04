import sys
script_arg=sys.argv[1]

   
def escalier(combien):
    for i in range(combien+1):
        print( " "*(combien - i) + "#"*i)


escalier(int(script_arg)) 