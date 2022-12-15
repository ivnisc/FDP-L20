import datetime
from pedido import numeroPedido
import os
from path import ruta_de_

def guardarFecho(path):
    fecho = datetime.datetime.now()
    fecho = fecho.strftime("%H:%M:%S %d/%m/%Y")  

    if os.path.exists(ruta_de_("historial.txt")):
        with open(ruta_de_("historial.txt"), 'a') as historial:
            historial.write(fecho + ' ' + numeroPedido(path) + '\n')
    else:
        with open(ruta_de_("historial.txt"), 'w') as historial:
            historial.write(fecho + ' ' + numeroPedido(path) + '\n')  


def leerHistorial():
    with open(ruta_de_("historial.txt"), 'r') as historial:
        for linea in historial:
            print(linea, end='')
    
# tests                       
#path = colocar ruta absoluta de algun archivo aquí
#guardarFecho(path)
#leerHistorial()
