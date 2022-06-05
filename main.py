#############################################
# Mauricio Lopez - @Morris-py
# Matías Cajal - @claaj
# UNRN Andina - Introducción a la Ingenieria en Computación - 2022
# TP Final
################
saldo_pesos = 85000
conv_soles = 0.04193
verificado = 0


def verificacion ():
    global verificado
    intentos = 0
    clave = 0
    dni_o = 12345678
    clave_o = 12345
    dni = 0
    while intentos < 3 and verificado != 1:
        print("intento número: "+ str(intentos+1))   
        clave = int(input("Ingrese su clave: "))
        if clave == clave_o:
            dni = int(input("Ingrese su DNI: "))
            if dni == dni_o:
                verificado = 1
                intentos = 3
            else:
                intentos = intentos + 1
        else:
            intentos = intentos + 1


def menuPrincipal ():
    """
    Función del menú principal del cajero.
    """
    opcion = 0
    while opcion != 4:
        opcion = int(input('1)Consultas 2)Retiros 3)Transferencias 4)Salir:'))
        if opcion == 1:
            print('Consultas')
            consultas()
        elif opcion == 2:
            print('Retiros')
        elif opcion == 3:
            print('Transferencia')





#Main
if __name__ == '__main__':
    print('Hola mundo!') 
    verificacion()
    if verificado == 1:
        menuPrincipal()
    else:
        print("Su tarjeta ha sido retenida")
    print('Programa finalizado!')

