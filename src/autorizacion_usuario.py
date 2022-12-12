import os
import sys
import pandas as pd

def ruta_csv():
    docs_path = os.path.join(os.path.dirname(sys.path[0]), "docs")
    csv_path = os.path.join(docs_path, "registro.csv")
    return csv_path

def crear_registro():
    datos = [[1,"", ""], [2,"", ""], [3,"", ""], [4,"", ""], [5,"", ""],
            [6,"", ""], [7,"", ""], [8,"", ""], [9,"", ""], [10,"", ""],]
    columnas = ["id", "nombre", "contraseña"]
    tipos_de_datos = {"id": "int", "nombre": "str", "contraseña": "str"}
    registro = pd.DataFrame(datos, columns=columnas).astype(tipos_de_datos)
    #registro.to_csv("registro.csv", index=False)
    #registro.to_csv(os.path.join(sys.path[0], "registro.csv"), index = False)
    registro.to_csv(ruta_csv(), index=False)


#funcion que recibe el nombre, contraseña e ingresa la cuenta al registro
def registrar_usuario(nombre, contraseña):
    nombre = nombre.capitalize()
    #sys.path[0] es la direccion del script, os.path.join une la direccion con el nombre del archivo
    #se lee el excel de la direccion correspondiente y se convierte a dataframe

    #si el archivo csv no existe, cuya ruta es ruta_csv(), se crea
    if not os.path.exists(ruta_csv()):
        crear_registro()


    #registro = pd.read_csv("registro.csv")
    #registro = pd.read_csv(os.path.join(sys.path[0], "registro.csv"), sep=",", encoding="utf-8")
    registro = pd.read_csv(ruta_csv(), sep=",", encoding="utf-8")

    #el ciclo va a comprobar en el dataframe que hayan espacios vacios
    #un espacio vacio en excel se representa como nan, hay que pasarlo a string para hacer comparativas
    i = 0
    escritura = True
    while i < 10 and escritura:
        #at[numero de fila, "columna"], revisa la posición de un dataframe
        if str(registro.at[i, "nombre"]) == "nan":
            #si encuentra una posición vacia, escribe los datos del usuario
            registro.at[i, "nombre"] = str(nombre)
            registro.at[i, "contraseña"] = str(contraseña)
            #print("Usuario registrado")
            #la escritura ha sido hecha, ahora se rompe el ciclo
            escritura = False
        i += 1
    if i == 10 and escritura:
        print("no se pudo ingresar la cuenta al registro porque este se encuentra lleno")
    
    #se transforma el dataframe a csv
    #registro.to_csv("registro.csv", index=False)
    #registro.to_csv(os.path.join(sys.path[0], "registro.csv"), index = False)
    registro.to_csv(ruta_csv(), index=False)

#funcion que recibe el nombre de una cuenta y la elimina del registro
def eliminar_cuenta(nombre):
    nombre = nombre.capitalize()

    #registro = pd.read_csv("registro.csv")
    #registro = pd.read_csv(os.path.join(sys.path[0], "registro.csv"), sep=",", encoding="utf-8")
    registro = pd.read_csv(ruta_csv(), sep=",", encoding="utf-8")

    i = 0
    escritura = True
    while i < 10 and escritura:
        if str(registro.at[i, "nombre"]) == nombre:
            registro.at[i, "nombre"] = ""
            registro.at[i, "contraseña"] = ""
            #print("Usuario eliminado")
            escritura = False
        i += 1
    
    #registro.to_csv("registro.csv", index=False)
    #registro.to_csv(os.path.join(sys.path[0], "registro.csv"), index = False)
    registro.to_csv(ruta_csv(), index=False)

#funcion que recibe nombre y contraseña, cambia la contraseña de un usuario
def cambiar_contraseña(nombre, contraseña):
    nombre = nombre.capitalize()

    #registro = pd.read_csv("registro.csv")
    #registro = pd.read_csv(os.path.join(sys.path[0], "registro.csv"), sep=",", encoding="utf-8")
    registro = pd.read_csv(ruta_csv(), sep=",", encoding="utf-8")

    i = 0
    escritura = True
    while i < 10 and escritura == True:
        if str(registro.at[i, "nombre"]) == nombre:
            registro.at[i, "contraseña"] = str(contraseña)
            #print("Contraseña cambiada")
            escritura = False
        i += 1
            
    #registro.to_csv("registro.csv", index=False)
    #registro.to_csv(os.path.join(sys.path[0], "registro.csv"), index = False)
    registro.to_csv(ruta_csv(), index=False)

#funcion que comprueba que la cuenta ingresada exista
def inicio_sesion(nombre, contraseña):
    nombre = nombre.capitalize()
    if nombre == "" or contraseña == "":
        print("Ingrese un usuario valido")

    #registro = pd.read_csv("registro.csv")
    #registro = pd.read_csv(os.path.join(sys.path[0], "registro.csv"), sep=",", encoding="utf-8")
    registro = pd.read_csv(ruta_csv(), sep=",", encoding="utf-8")

    i = 0
    escritura = True
    while i < 10 and escritura:
        if str(registro.at[i, "nombre"]) == nombre and str(registro.at[i, "contraseña"]) == contraseña:
            print("sesion iniciada")
            escritura = False
        i += 1
    if i == 10 and escritura == True:
        print("sesion no iniciada")

