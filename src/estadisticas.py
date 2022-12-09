#es necesario tener descargado el archivo inventario.csv

#librerias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#archivo
df = pd.read_csv("inventario.csv")

"""
El histograma esta hecho principalmente para variables solo numericas,
asi q se recomienda solo ocuparlo con la columna "Largo"
"""
def histograma(variable):
    if variable=="Largo":
        plt.hist(df[variable],100,color="r",ec="black")
        plt.title("histograma"+ variable)
        return plt.show()
    else:
        return "No se pudo realizar el grafico"


"""
El grafico de barras se puede ocupar con cualquier columna
ya que solo muestra la cantidad de repeticiones de cada dato,
aunque con la columna "Largo" no es recomendable(son muchos datos)
"""

def grafico_de_barras (variable):
    if variable != "" or None:
        if variable == "Perfil" or "Largo" or "Ubicación" or "Color" or "Usuario":
            df[variable].value_counts().plot(kind="bar",
            title= variable,xlabel="Tipo",ylabel="Cantidad", color="c")
            return plt.show()
    else:
        return "No se pudo realizar el grafico"

"""
El grafico circular calcula los porcentajes de cada dato,
es recomendable ocuparlo con los datos de los usuarios

"""

def grafico_circular (variable):
    if variable != "" or None:
        if variable == "Perfil" or "Largo" or "Ubicación" or "Color" or "Usuario":
            df[variable].value_counts().plot(kind="pie",autopct="%2f%%",title="Porcentaje de "+ variable)
            return plt.show()
    else:
        return "No se pudo realizar el grafico"

"""
Grafico multiple: si en la colum1 se ingresa la columna "usuario" y la colum2 se ingresa
"perfil", muestra el numero de "perfiles" que ha ingresado cada usuario
Es recomendable que la colum1 siempre sea el usuario
"""

def grafico_multiple (colum1,colum2):
    if colum1 or colum2 != "" or None:
        if colum1 and colum2 == "Perfil" or "Largo" or "Ubicación" or "Color" or "Usuario":
            x=df.groupby([colum1,colum2]).size()
            x=x.reset_index()
            x=pd.pivot_table(x,columns=colum1,index=colum2)
            x.plot(kind="bar",title= "Numero de "+ colum2+" elegido por cada "+ colum1)
            return plt.show()
    
    else:
        return "no se pudo realizar el grafico"

#segunda funcion

"""
Esta función filtra a los usuarios por su nombre y entrega un dataframe con
las acciones que ha realizado 
"""
def acciones_usuarios (nombre):
    accion=df[(df["Usuario"]== nombre)]
    if accion.empty:
        return "no hay coincidencias"
    else:
        return accion

        
print(acciones_usuarios("XD"))