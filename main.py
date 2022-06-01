#############################################
# Mauricio .... - @.....
# Matías Cajal - @claaj
# UNRN Andina - Introducción a la Ingenieria en Computación - 2022
# TP Final
################

def menuPrincipal ():
    """
    Función del menú principal del cajero.
    """
    opcion = 0
    while opcion != 4:
        opcion = int(input('1)Consultas 2)Retiros 3)Transferencias 4)Salir:'))
        if opcion == 1:
            print('Consultas')
        elif opcion == 2:
            print('Retiros')
        elif opcion == 3:
            print('Transferencia')

#Main
if __name__ == '__main__':
    print('Hola mundo!')
    menuPrincipal()
    print('Programa finalizado!')
