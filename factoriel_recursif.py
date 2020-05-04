import sys
arg_shell=sys.argv[1]
def factoriel_recurs(n):
    if n==1:
        return 1
    else:
        return n * factoriel_recurs(n-1)
        
print(factoriel_recurs(int(arg_shell)))        