# Definició de funcions auxiliars
# Funció del menú principal
def menu_principal():
    print("""Calculadora
        Menú
        1. Números enters
        2. Números reals
        3. Canvis de base
        0. Sortir
    """)
    opcio=input("Seleccioni l'opció que vulguis: ")
    return opcio

# Funció del menú de números enters
def menu_enters():
    print ("""
        Menú calculadora de números enters:
        1. Sumar
        2. Restar
        3. Multiplicar
        4. Dividir
        0. Sortir
    """)   
    opcio=input("Selecicioni l'opció que vulgui")
    return opcio    

# Funció de nombres binaris
def menu_nombres_binaris():
 	print("""
        Menú calculadora canvis de base:
        1. Donat un binari passar a octal, decimal i hexadecimal.
        2. Donat un octal passar a binari, decimal i hexadecimal.
        3. Donat un decimal passar a binari, octal i hexadecimal.
        4. Donat un hexadecimal passar a binari, octal i decimal.
        0. Sortir
	""")
#Programa principal de la calculadora
opcio=1
while(opcio!=0):
    opcio= menu_principal()
    match opcio:
        case "1": 
            opcio2=menu_enters
            a = int(input("Indiqui el primer operand: "))
            b = int(input("Indiqui el segon operand: "))
            match opcio:
                case "1":
                    c=a+b
                    print("La suma de ",a," més ",b," és ",c)
                case "2":
                    c=a-b
                    print("La resta de ",a," menos ",b," és ",c)
                case "3":
                    c=a*b
                    print("La multiplicació de ",a," per ",b," és ",c)
                case "4":
                    c=a/b
                    print("La divisió de ",a," dividid ",b," és ",c)
                case "0":
                    print("Adeú")
                case other:
                    print("Opció no vàlida!")
        case "2":
            print ("""
        Menú calculadora de números enters:
        1. Sumar
        2. Restar
        3. Multiplicar
        4. Dividir
        0. Sortir
        """)   
            a = int(input("Indiqui el primer operand: "))
            b = int(input("Indiqui el segon operand: "))
            match opcio:
                case "1":
                    c=a+b
                    print("La suma de ",a," més ",b," és ",c)
                case "2":
                    c=a-b
                    print("La resta de ",a," menos ",b," és ",c)
                case "3":
                    c=a*b
                    print("La multiplicació de ",a," per ",b," és ",c)
                case "4":
                    c=a/b
                    print("La divisió de ",a," dividid ",b," és ",c)
                case "0":
                    print("Adeú")
                case other:
                    print("Opció no vàlida!")
        case "3":
            print ("""
        Menú calculadora canvis de base:
        1. Doant un binari passar a octal, decimal i hexadecimal.
        2. Donat un octal passar a binari, decimal i hexadecimal.
        3. Donat un decimal passar a binari, octal i hexadecimal.
        4. Donat un hexadecimal passar a binari, octal i decimal.
        0. Sortir
        """)   
            a = int(input("Indiqui el primer operand: "))
            b = int(input("Indiqui el segon operand: "))
            match opcio:
                case "1": # Binari a
                    c=a+b
                    print("La suma de ",a," més ",b," és ",c)
                case "2":
                    c=a-b
                    print("La resta de ",a," menos ",b," és ",c)
                case "3":
                    c=a*b
                    print("La multiplicació de ",a," per ",b," és ",c)
                case "4":
                    c=a/b
                    print("La divisió de ",a," dividid ",b," és ",c)
                case "0":
                    print("Adeú")
                case other:
                    print("Opció no vàlida!")