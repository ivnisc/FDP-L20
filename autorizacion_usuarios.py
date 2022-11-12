import os
import sys
import pandas as pd


#Funcion que recibe el nombre, contraseña y numero de cuenta e ingresa la info al dataframe
def registrar_usuario(nombre, contraseña):
    #sys.path[0] es la direccion del script, os.path.join une la direccion con el nombre del archivo
    #se lee el excel de la direccion correspondiente y se convierte a dataframe
    registro = pd.read_excel(os.path.join(sys.path[0], "registro.xlsx"))
    #el ciclo va a comprobar en el dataframe que hayan espacios vacios
    #un espacio vacio en excel se representa como nan, hay que pasarlo a string para hacer comparativas
    i = 0
    escritura = True
    while i < 11 and escritura:
        #at[numero de fila, "columna"], revisa la posición de un dataframe
        if str(registro.at[i, "nombre"]) == "nan":
            #si encuentra una posición vacia, escribe los datos del usuario
            registro.at[i, "nombre"] = nombre
            registro.at[i, "contraseña"] = contraseña
            #la escritura ha sido hecha, ahora se rompe el ciclo
            escritura = False
        i += 1
    #se transforma el dataframe a excel
    with pd.ExcelWriter(os.path.join(sys.path[0], "registro.xlsx")) as writer:
        registro.to_excel(writer, index = False)
    
# falta la funcion de lectura, comprobar que haya un usuario
# falta la funcion de eliminar una cuenta
# modificar funcion registrar_usuario

