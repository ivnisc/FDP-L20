import datetime
from pedido import numeroPedido

def guardarFecho(path):
    fecho = datetime.datetime.now()
    fecho = fecho.strftime("%H:%M:%S %d/%m/%Y")    
    with open("../docs/historial.txt", 'a') as historial:
        historial.write(fecho + ' ' + numeroPedido(path) + '\n')

def leerHistorial():
    with open("../docs/historial.txt", 'r') as historial:
        for linea in historial:
            print(linea, end='')
    
# test                        
#path = "/Users/u/Desktop/lab/project/docs/zolezzi.pdf"
#guardarFecho(path)
#leerHistorial()

# considerar
# ruta del archivo historial.txt en windows es distinta a la de mac.
# ruta relativa en windows es: "..\\docs\\historial.txt" creo.

