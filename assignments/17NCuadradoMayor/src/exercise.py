def main():
    numero = int(input("Escribe un numero : "))
    #escribe tu código abajo de esta línea
    c=1
    while c**2<=numero:
        c=c+1
    print(c)

if __name__=='__main__':
    main()
