"""Pide la edad y el nombre por teclado. En caso de ser mayor de 18 años indica que ya puede conducir."""

def main():
    nombre=str(input("Introduzca su nombre: "));
    edad=int(input(f"Introduzca su edad {nombre}: "))

    # Comprobamos si es mayor de edad - Estructura condicional if - else
    # Si edad mayor o igual a dieciocho --> Usted es nayor de edad
    # Sino --> Todavía eres menor de edad


    if edad >=18:
        print("Usted es mayor de edad")
        return True
    else:
        print("Todavía eres menor de edad")
        return False



if __name__== "__main__" :
    main()
