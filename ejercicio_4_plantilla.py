def sumar(primer_numero, segundo_numero):
    return primer_numero + segundo_numero


def restar(primer_numero, segundo_numero):
    return primer_numero - segundo_numero
    


def multiplicar(primer_numero, segundo_numero):
    return primer_numero * segundo_numero
    


def dividir(primer_numero, segundo_numero):
    return primer_numero / segundo_numero
    

def es_par(numero):
    return numero % 2
    

def calculadora():
        print("\n--- CALCULADORA ---")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Verificar si un número es par")
        print("6. Salir")
        
#-------------------------------------------------------------------------------


while True:
   
    calculadora()
    opcion = input("Elige una opción: ")

    match opcion:

         case 1: 
         