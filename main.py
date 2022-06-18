#############################################
# Mauricio Lopez - @Morris-py
# Matías Cajal - @claaj
# UNRN Andina - Introducción a la Ingeniería en Computación - 2022
# TP Final
################
import random

saldo_pesos = 85000.00
conv_soles = 0.04193
verificado = 0
cuenta = 0.00
monto = 0.00
moneda = ""
cuenta_destino = 98765
monto_ok = False
clave_o = 12345

def cuentaSaldo():
    global moneda, cuenta, saldo_pesos
    if moneda == 'pesos':
        saldo_pesos = cuenta
    else:
        saldo_pesos = cuenta / conv_soles

def transferencias():
    global cuenta, moneda, monto, monto_ok
    eleccionMoneda()
    ingresoMonto()
    if monto_ok == True:
        cuenta_transf = int(input('Ingrese cuenta de destino: '))
        if cuenta_destino == cuenta_transf:
            cuenta = cuenta - monto
            print('Operación exitosa')
        else:
            cuenta -= monto
            print('Cuenta errónea, en 3 días visualizará la devolución en sus "Movimientos"')
        cuentaSaldo()
    else:
        print('Monto inválido, volviendo al menú.')

def ingresoMonto ():
    global cuenta, moneda, monto, monto_ok
    monto = 0.00
    monto_ok = False
    intentos = 0
    salida = False
    while salida != True:
        intentos += 1
        monto = float(input(f'Ingresar monto en {moneda}: '))
        if monto <= cuenta:
            monto_ok = True
            salida = True
        elif intentos == 2:
            salida = True
        else:
            print('No tiene suficiente saldo para realizar esta operación.')
            monto_salir = int(input('1)Ingresar un nuevo monto 2)Salir al menu inicial: '))
            if monto_salir == 2:
                salida = True

# Función retiros principal
def retiros ():
    global cuenta, moneda, clave_o, monto_ok
    eleccionMoneda()
    ingresoMonto()
    if monto_ok == True:
        clave_retiro = int(input('Ingrese su clave: '))
        if clave_retiro == clave_o:
            cuenta = cuenta - monto
            cuentaSaldo()
            imp_ticket = int(input("1)Ticket 2)Ver en pantalla: "))
            if imp_ticket == 1:
                print("Ticket impreso, retírelo")
            else:
                print(f'Retiro en {moneda} de: {monto}')
        else:
            print('Clave incorrecta, retiro cancelado')
    else:
        print('Monto inválido, volviendo al menú.')

def verificacion ():
    global verificado, clave_o
    intentos = 0
    clave = 0
    dni_o = 12345678
    dni = 0
    salida = False
    while salida != True:
        print(f"Intento N°{intentos+1}")
        clave = int(input("Ingrese su clave: "))
        if clave == clave_o:
            dni = int(input("Ingrese su DNI: "))
            if dni == dni_o:
                verificado = True
                salida = True
            else:
                intentos = intentos + 1
        else:
            intentos = intentos + 1
        if intentos == 3:
            salida = True

def menuPrincipal ():
    """
    Función del menú principal del cajero.
    """
    opcion = 0
    while opcion != 4:
        opcion = int(input('1)Consultas 2)Retiros 3)Transferencias 4)Salir: '))
        if opcion == 1:
            print('Consultas')
            consultas()
        elif opcion == 2:
            print('Retiros')
            retiros()
        elif opcion == 3:
            print('Transferencia')
            transferencias()
        elif opcion == 4:
            print('Saliendo...')
            print('Retire su tarjeta, Gracias por utilizar nuestros servicios!')
        else:
            print('Opción incorrecta, intente nuevamente')

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

def movimientos():
    opcion_ok = False
    i = 0
    while opcion_ok != True:
        elegir_mon = int(input('1)Pesos 2)Soles: '))
        if elegir_mon == 1:
            while i < 10:
                print(f'{random.uniform(99,9999):.2f} pesos')
                i += 1
            opcion_ok = True
        elif elegir_mon == 2:
            while i < 10:
                print(f'{(random.uniform(99,9999)*0.04193):.2f} soles')
                i += 1
            opcion_ok = True
        else:
            print('Opción incorrecta, intente nuevamente')

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
            print(f"Tu cuenta en {moneda} es de {cuenta:.2f}.")
    else:
        movimientos()

#Main
if __name__ == '__main__':
    print('Bienvenido al Banco InterBanca!')
    verificacion()
    if verificado == 1:
        menuPrincipal()
    else:
        print("Su tarjeta ha sido retenida")
