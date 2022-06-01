# TP Final de Introducción a Ingeniería en Computación

La consigna del trabajo práctico final es:

Retrocedemos en el tiempo, y estamos en el año 1985. El banco InterBanca, es una entidad financiera que opera tanto en Perú como en Argentina. A la fecha tiene muchas quejas por parte de sus clientes, con respecto al formato de trabajo de sus agencias bancarias. Por este motivo, desean innovar usando cajeros automáticos. Los cajeros automáticos requieren de programación y para ello, los han contratado a ustedes. Así, su misión consiste en diseñar y desarrollar un algoritmo que tenga en cuenta el siguiente manejo del cajero:

- A) El cliente presiona el botón de activación, y de esta manera se solicita el ingreso de su tarjeta.

- B) El cliente inserta su tarjeta en la ranura. El algoritmo del cajero automático lee la información de la tarjeta y luego solicita la clave de acceso.

- C) El cliente ingresa su clave de acceso, la cual es verificada con la base de datos del banco. Si es correcta le solicitará el número del DNI y también se validará contra la Base de datos. En caso de ser correcto se le presentará en pantalla el menú de opciones. En caso de que haya superado más 3 intentos fallidos de ingreso de la clave de acceso, el cajero retendrá la tarjeta.

- D) El menú de opciones tiene las siguientes funcionalidades:

  1. Consultas.
  
  2. Retiros.
  
  3. Transferencias.
  
  4. Salir.

- E) El cliente revisará las opciones y en base a su requerimiento, selecciona una opción.

- F) Si el cliente selecciona la opción 1, le permitirá consultar sus cuentas, teniendo dos opciones: 
  
  - Posición GLOBAL: es el Saldo disponible. 
  
  - Movimientos: mostrará los últimos 10 movimientos (generados al azar).
  
  En cualquiera de ambos casos, se debe solicitar el tipo de moneda (“Soles” / “Pesos”). Además, el usuario podrá elegir entre visualizar la consulta en pantalla o imprimir el reporte. Luego de ello se finalizará la operación. En caso de que requiera realizar otra operación deberá regresar al paso e.

- G) Si el cliente selecciona la opción 2, el cajero le solicitará el tipo de moneda (“Soles” / “Pesos”) y el monto a retirar, para luego solicitar la cuenta a debitar. El cajero verifica la disponibilidad de saldo, en el caso de que no tenga saldo disponible, se le mostrará un mensaje y le permitirá modificar el monto “sólo por una vez”, o salir de la transacción. Para el caso de contar con disponibilidad, el cajero solicita nuevamente que ingrese la clave de acceso, y pregunta si desea impresión de voucher o no, luego finaliza la operación. En caso de que requiera realizar otra operación deberá regresar al paso e.

- H) Si el cliente selecciona la opción 3, el cajero solicita el número de cuenta destino, el tipo de moneda (“Soles” / “Pesos”) y el monto a transferir. Se debe verificar la disponibilidad del saldo de su cuenta. Además, si el número de la cuenta de destino no es correcto, recién después de tres días el cliente podrá observar la devolución de su dinero en sus “movimientos”. Luego finaliza la operación. En caso de que requiera realizar otra operación deberá regresar al paso e.

- I) Si el cliente selecciona la opción 4, se finaliza la transacción en el cajero y se expulsa la tarjeta.
  **Nota:** Para poner a prueba el programa implementado, teniendo en cuenta que no estamos manejando Base de Datos, se probará contra el siguiente usuario registrado.
  - **Clave:** 12345
  - **DNI:** 12345678
  - **Cuenta de destino en la cual se hará la transferencia:** 98765
  - **Saldo de la cuenta:** en Pesos Argentinos 85.000 (en Soles Peruanos 3.564)
  Esta información se mantendrá constante (a excepción del saldo) durante la ejecución del algoritmo.
