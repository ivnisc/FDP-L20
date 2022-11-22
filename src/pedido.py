import PyPDF2
import re
import pandas as pd
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

"""
La función leerPDF retorna un formato trabajable de las ventanas del pedido
del cliente. Comienza extrayendo la información en texto plano, para luego
darle un formato conveniente. La lógica que se utilizó fue la siguiente: 

Cada ventana tiene 4 lados, con ancho y largo. Primero conseguimos listar
cada una de ellas, tomando la cantidad, perfil, color y largo X ancho,
es decir, deshacernos del contenido del pdf que no sirve y obtener la tabla
de artículos comprados.

Si el cliente compró una misma ventana (con las mismas dimensiones) en
varias cantidades, se clona el mismo elemento por esa cantidad, para así
deshacernos de la columna cantidad. Ejemplo:

Cantidad 5 | ventana fija | color caoba | largo = 200.2 x ancho = 100.9
resulta en hacer 5 filas de ventana fija | color caoba | ... .

El siguiente paso es crear por cada una de estas, dos filas en un nuevo
dataframe: Una fila con la longitud del largo de la ventana, y la 2da fila,
con el ancho como largo del PVC. Al fin y al cabo, al desarmar una ventana,
tods los lados tienen cierta longitud.

Entonces para una ventana como el ejemplo anterior, el dataframe es algo así:

FIJA, CAOBA, 200.2
FIJA, CAOBA, 100.9
FIJA, CAOBA, 200.2
FIJA, CAOBA, 100.9

Para el caso en que la boleta pdf dice que son n cantidades de esta, las 4 filas
se repetirían n veces. En conclusión, cada ventana de manera individual significa
4 filas en el dataframe final. Un pdf con un pedido de 10 ventanas, se traduce en
un dataframe de 40 filas, de las cuales para cada una debemos averiguar si tienen
un residuo disponible en el inventario que podamos reutilizar. 
"""

def leerPDF(path):
    with open(path, 'rb') as f:
        pdf = PyPDF2.PdfFileReader(f)
        lista_elementos = []
        for page in pdf.pages:
            lines = page.extractText().splitlines()
            for i in range(len(lines)):
                # Este regex es análogo a un simple "perfil" in lines[i] or ...
                if re.search(r"FIJA|BATIENTE|CORREDERA|OSCILANTE", lines[i]):
                    lista_elementos.append(lines[i])

    auxlist = []

    for i in range(len(lista_elementos)):
        # Esto quita un espacio si este se encuentra antes o después de un punto.
        lista_elementos[i] = re.sub(r"\.\s|\s\.", ".", lista_elementos[i])
        
        # Quita un espacio si este está entre dos dígitos,
        # para casos en que una medida estaba como el siguiente ejemplo.
        # 2 35.5  => 235.5      ;
        lista_elementos[i] = re.sub(r"(\d)\s(\d)", r"\1\2", lista_elementos[i])

        # Ahora cortamos la cadena en la posición de 6 caracteres después de encontrar "X".
        # Esto funciona porque el formato de un elemento de la boleta siempre será el siguiente:
        # [cant]_[perfil]_[color]_[largo(nnn.n)]_["X"]_[ancho(nnn.n)]_[p.unitario]_[p.acumulado]
        # por lo no es de importancia que el regex anterior junte el ancho con el precio unitario.
        lista_elementos[i] = lista_elementos[i][:lista_elementos[i].find("X")+7]

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
        
def match(dfpdf, dfinv, user):

    # Se usarán dos dataframes con columnas del inventario.
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
                    dfinv.iloc[k, 2] == dfcand.iloc[0, 2]):
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
    dfinv.to_csv("inventario.csv", index=False)
    # Retornamos el match, sin la columna usuario ya que no se necesita.
    
    return dfmatch.iloc[:, 0:4]
    

# Líneas de prueba para la consola. El argumento "XD" debería tener una función estilo
# get.User() el cual obtiene de la interfaz, el String del usuario que inició sesión.

print(leerPDF("/Users/u/Desktop/lab/project/docs/meruane.pdf"))
print( "-----------------------------------------")
print(match(leerPDF("/Users/u/Desktop/lab/project/docs/meruane.pdf"), pd.read_csv("inventario.csv"), "XD"))



