import pandas as pd
from random import randint
from path import ruta_de_

def nuevoElemento(profile, kolor, largue, location):
    df = pd.read_csv(ruta_de_("inventario.csv"))
    if profile != "" or kolor != "" or largue != "" or location != "":
        return "No puede haber campos vacíos"
    else: 
        df.loc[len(df)] = [profile, kolor, largue, location, "uwu"]
        df.to_csv(ruta_de_("inventario.csv"), index=False)

def deshacer():
    df = pd.read_csv(ruta_de_("inventario.csv"))
    df = df[:-1]
    df.to_csv(ruta_de_("inventario.csv"), index=False)

def filtrarElementos(profile, kolor, largue, location):
    df = pd.read_csv(ruta_de_("inventario.csv"))
    if profile != "" or None:
        df = df[df.Perfil == profile]
    if kolor != "" or None:
        df = df[df.Color == kolor]
    if largue != "" or None:
        if "-" in largue:
            largue = largue.split("-")
            df = df[(df.Largo >= float(largue[0])) & (df.Largo <= float(largue[1]))]
        else:
            df = df[df.Largo == float(largue)]
    if location != "" or None:
        df = df[df.Ubicación == location]
    # En las siguientes dos líneas se quitan los elementos que ya fueron usados (con usuario)
    # luego se remueve la columna usuario ya que no se debe visualizar en el filtro     ;
    df = df.drop(df[df.Usuario != "uwu"].index)
    df = df.drop(columns= "Usuario")  
    if df.empty:
        return "No se encontraron elementos con esas características."
    else:
        return df
