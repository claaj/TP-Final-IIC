#############################################
# Mauricio Lopez - @Morris-py
# Matías Cajal - @claaj
# UNRN Andina - Introducción a la Ingenieria en Computación - 2022
# TP Final
################
saldo_pesos = 85000
conv_soles = 0.04193
verificado = 0
cuenta = 0
moneda = ""

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

def eleccionMoneda ():
    global cuenta, moneda
    elegir_mon = 0
    elegir_mon = int(input("1)Pesos 2)Soles: "))
    if elegir_mon == 1:
        cuenta = saldo_pesos
        moneda = "pesos"
    else:
        cuenta = saldo_pesos * conv_soles
        moneda = "soles"

def consultas ():
    opcion_con = 0
    imp_ticket = 0
    opcion_con = int(input("1)Posición Global 2)Movimientos: "))
    if opcion_con == 1:
        eleccionMoneda()
        imp_ticket = int(input("1)Ticket 2)Ver en pantalla: "))
        if imp_ticket == 1:
            print("Ticket impreso, retírelo")
        else:
            print(f"Tu cuenta en {moneda} es de {cuenta}.")




#Main
if __name__ == '__main__':
    print('Hola mundo!') 
    verificacion()
    if verificado == 1:
        menuPrincipal()
    else:
        print("Su tarjeta ha sido retenida")
    print('Programa finalizado!')

