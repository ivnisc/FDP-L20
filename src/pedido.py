import PyPDF2
import re
import pandas as pd
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
from path import ruta_de_

"""
La función leerPDF utiliza la librería PyPDF2 para leer el archivo PDF.
Esta lectura se realiza página por página (si es que tiene más de una), 
y luego línea por línea. El archivo contiene mucho texto que no es de interés,
por lo que se utiliza una expresión regular simple para encontrar las 
líneas que contienen el perfil de la ventana, el color, el largo y el ancho.

Estas líneas se guardan en una lista llamada lista_elementos.
Se recorre dicha lista para corregir algunos errores de formato en los 
que la librería puede fallar al detectar los caracteres.

Por ejemplo, en el caso de que el largo o el ancho de la ventana esté compuesto
de dos dígitos, la librería puede leerlo como "2 35.5" en lugar de "235.5".
Esto se soluciona con un regex que elimina el espacio entre dos dígitos.
Luego se recorre la lista para eliminar el precio unitario y el precio 
acumulado, cortando el string.

El resultado final es una lista cuyos elementos son idénticos a la descripción
de las ventanas que se muestran en el archivo pdf.
"""

def leerPDF(path):
    with open(path, 'rb') as f:
        pdf = PyPDF2.PdfFileReader(f)
        lista_elementos = []
        for pagina in pdf.pages:
            linea = pagina.extractText().splitlines()
            for i in range(len(linea)):
                # Este regex es análogo a un simple "perfil" in lines[i] or ...
                if re.search(r"FIJA|BATIENTE|CORREDERA|OSCILANTE", linea[i]):
                    lista_elementos.append(linea[i])

    for i in range(len(lista_elementos)):
        # regex que quita un espacio si este se encuentra antes o después de un punto.
        lista_elementos[i] = re.sub(r"\.\s|\s\.", ".", lista_elementos[i])
        
        # regex que quita un espacio si este está entre dos dígitos,
        # para casos en que una medida estaba como el siguiente ejemplo.
        # 2 35.5  => 235.5      ;
        lista_elementos[i] = re.sub(r"(\d)\s(\d)", r"\1\2", lista_elementos[i])

        # Ahora cortamos la cadena en la posición de 6 caracteres después de encontrar "X".
        # Esto funciona porque el formato de un elemento de la boleta siempre será el siguiente:
        # [cant]_[perfil]_[color]_[largo(nnn.n)]_["X"]_[ancho(nnn.n)]_[p.unitario]_[p.acumulado]
        # por lo no es de importancia que el regex anterior junte el ancho con el precio unitario.
        lista_elementos[i] = lista_elementos[i][:lista_elementos[i].find("X")+7]

    return lista_elementos

"""
La función dataFramePedido usa la lista de elementos que devuelve la función leerPDF.
Lo que hace es "descomponer" cada elemento de la lista según cantidad y medida.

Por ejemplo, si un elemento de la lista tiene cantidad 4, queremos que el dataframe
tenga 4 filas con la misma descripción de dicho elemento.

Luego de esto, queremos dividir nuevamente cada uno de estos, descomponiendo 
cada uno en una copia con el largo y otra con el ancho.
Pero como una ventana tiene 4 lados, corresponde crear 2 copias del elemento 
con el largo y dos copias del elemento con el ancho.
Entonces, para un solo elemento único, se crean 4 copias, 1 por cada lado de la ventana.

El return de esta función es un dataframe con los elementos descompuestos, listos para
buscar candidatos en el inventario y reutilizarlos en la fabricación de la ventana.
"""

def dataFramePedido(lista_elementos):   
    auxlist = []
    for i in range(len(lista_elementos)):
        # En auxlist insertamos el elemento tantas veces como la cantidad que lo acompaña indique.
        for j in range(int(lista_elementos[i][0])):
            auxlist.append(lista_elementos[i][2:])

    # Iteramos sobre la lista auxiliar.
    # Cada línea tiene un largo y ancho separado por " X ".
    # Entonces desde auxlist, insertamos en auxlist2 todo el elemento excepto el ancho.
    # Luego hacemos lo mismo pero excepto el largo.  
    auxlist2 = []
    for j in range(len(auxlist)):
        auxlist2.append(auxlist[j][:auxlist[j].find("X")-1])
        auxlist2.append(auxlist[j][:auxlist[j].find("X")-6] + 
        auxlist[j][auxlist[j].find("X")+2::])
        # Realizamos este proceso dos veces cada una, para obtener 4 copias del elemento.
        # Una por cada lado de la ventana.
        auxlist2.append(auxlist[j][:auxlist[j].find("X")-1])
        auxlist2.append(auxlist[j][:auxlist[j].find("X")-6] + 
        auxlist[j][auxlist[j].find("X")+2::])

    auxlist2, lista_elementos = lista_elementos, auxlist2

    # Para el caso particular en que el color está compuesto de dos palabras, 
    # como por ejemplo "ROBLE CLARO" o "ROBLE OSCURO",
    # las juntamos como un solo elemento de la lista.
    # De paso aprovechamos de crear una lista de listas, para la creación del dataframe.
    for v in range(len(lista_elementos)):
        lista_elementos[v] = lista_elementos[v].split()
        if "ROBLE" in lista_elementos[v]:
            lista_elementos[v][1] = lista_elementos[v][1] + " " + lista_elementos[v][2]
            lista_elementos[v].pop(2)   
    df = pd.DataFrame(lista_elementos, columns=["Perfil", "Color", "Largo"])
    df["Largo"] = df["Largo"].astype(float)

    return df

"""
La función match (de la funcionalidad buscar residuos de PVC),
retorna un dataframe casi idéntico al de los elementos del pedido, pero con
la distinción de entregar el residuo del inventario ideal para ser usado
en la fabricación de dicha ventana. 

Para cada elemento del dataframe del pedido, se recorre todo el inventario,
buscando candidatos posibles para su utilización. 

Una vez se tienen todos los candidatos, se elije el que tiene la longitud más
cercana al largo de la ventana que se quiere fabricar, con el fin de no utilizar
residuos demasiado largos que podrían servir para ventanas más grandes.

El residuo elegido se marca en el inventario con el nombre del usuario que está 
utilizando el software en ese momento (el que tiene sesión iniciada).
De esta manera dicho residuo deja de estar disponible ya que fue REutilizado
para fabricar una nueva ventana sin necesitar una viga de PVC nueva, reduciendo
la conservación de desechos industriales, Yei :D
"""

def match(dfpdf, user):
    # Se usarán dos dataframes con columnas del inventario.
    dfinv = pd.read_csv(ruta_de_("inventario.csv"))
    dfcand = pd.DataFrame(columns=dfinv.columns)
    dfmatch = pd.DataFrame(columns=dfinv.columns)
    # Creamos un índice al dfinv
    dfinv = dfinv.reset_index(drop=True)

    # Iterar sobre los elementos del pdf.
    for i in range(len(dfpdf)):
        # Iterar sobre el inventario.
        for j in range(len(dfinv)):
            # dfcand guarda todos los que del dfinv que coinciden con el elemento del pdf
            # con la condición más importante, que no hayan sido usados (== "uwu").
            
            if (dfpdf.iloc[i, 0] == dfinv.iloc[j, 0] and 
                dfpdf.iloc[i, 1] == dfinv.iloc[j, 1] and 
                dfinv.iloc[j, 4] == "uwu"):
                dfcand = dfcand.append(dfinv.iloc[j, :])

        # Descartamos los que tienen largo menor al elemento del pdf
        # ya que es imposible que sirvan.
        dfcand = dfcand[dfcand["Largo"] >= dfpdf.iloc[i, 2]]

        # Si resulta que existen PVC's usables (dfcand no vacío),
        # ordenamos de largo más cercano al elemento del pdf, hasta el más lejano.
        if not dfcand.empty:
            dfcand = dfcand.sort_values(by="Largo")

            # Agregamos a dfmatch el primer elemento ordenado, es decir, 
            # el de largo más cercano a la medida de la ventana que el pdf nos dice.
            dfmatch = dfmatch.append(dfcand.iloc[0, :])

            # Ahora necesitamos que ese mismo elemento que hemos guardado,
            # no siga disponible para el siguiente elemento i del pdf.

            # Entonces, en el dfinv buscamos el elemento que coincide con
            # el primero de dfcand (es decir, el elegido para ser usado). 
            for k in range(len(dfinv)):
                if (dfinv.iloc[k, 0] == dfcand.iloc[0, 0] and 
                    dfinv.iloc[k, 1] == dfcand.iloc[0, 1] and 
                    dfinv.iloc[k, 2] == dfcand.iloc[0, 2] and
                    dfinv.iloc[k, 3] == dfcand.iloc[0, 3]):
                    dfinv.iloc[k, 4] = user
                    break

            dfcand.iloc[0:0]

        else: 
            # dfcand vacío significa que en el inventario no hay piezas
            # para las características del elemento que está consultando.
            # Entonces solo agregar una línea vacía (se ve como NaN's)

            dfmatch = dfmatch.append(pd.Series(), ignore_index=True)
        
        # Limpiamos el dfcand para almacenar candidatos de la siguiente linea del pdf.
        dfcand = dfcand.iloc[0:0]

    # Guardamos las actualizaciones de usuario realizadas en el dfinv
    dfinv.to_csv(ruta_de_("inventario.csv"), index=False)
    # Retornamos el match, sin la columna usuario ya que no se necesita.
    
    return dfmatch.iloc[:, 0:4]

""" 
La función numeroPedido es similar a la leerPDF.
Se utiliza la librería PyPDF2 para leer el pdf y extraer el número de pedido.
Se recorre cada párrafo del pdf, buscando la frase "N.º DE BOLETA".
Una vez se encuentra, se retorna los últimos 3 caracteres del párrafo, que
corresponden al número del pedido.
"""

def numeroPedido(path):
    with open(path, 'rb') as f:
        pdf = PyPDF2.PdfFileReader(f)
        linea = pdf.pages[0].extractText().splitlines()
        for i in range(len(linea)):
            if "N.º DE BOLETA" in linea[i]:
                return linea[i][-4:-1]

"""
La función modificar color es llamada como un mensaje de confirmación al usuario.
Se le pregunta si desea modificar el color de alguna ventana, y si es así, se le pide
que ingrese el nuevo color, junto con el número de la ventana de la lista.
Se retorna la lista actualizada con el color modificado.
"""
      
def modificarColor(funcionleerPDF, kolor, index):
    lista_elementos = funcionleerPDF
    # el elemento de la lista es un string, así que lo convertimos a lista
    lista_elementos[index-1] = lista_elementos[index-1].split()
    # modificamos el color
    lista_elementos[index-1][2] = kolor
    # convertimos la lista a string
    lista_elementos[index-1] = " ".join(lista_elementos[index-1])
    return lista_elementos