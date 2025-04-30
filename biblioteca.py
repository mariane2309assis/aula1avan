def imprime_nome(nome):
    print(f"Nome:{nome}")

def piramide(n):
    for x in range(1, n + 1):
        for y in range(0, x):
            print(x, end=" ")
        print()

def contaVogais(texto):
    cont=0
    for x in range(len(texto)):
        if texto[x]== "a" or texto[x] == "e" or texto[x]=="i" or texto[x]=="o" or texto[x]=="u":
            cont=cont+1
    print(cont)

def estoque(produto, quantidade,valorUnitario):
    valorTotal=quantidade*valorUnitario
    return valorTotal

def numeros(n):
    for n in range(n):
        if n == 0:
            return "Z"
        elif n > 0:
            return"P"
        else:
            return"N"

def soma(a,b):
    res=a+b
    print(res)

def soma(*a):
    soma=0
    for x in range(len(a)):
        soma+=a[x]
    print(soma)

def textoReverso(t):
    cont=0
    for x in range(len(t)-1,-1,-1):
        print(t[x],end=" ")
        if t[x] !=" ":
            cont+=1
    print(t)