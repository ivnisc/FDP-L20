import pandas as pd

def nuevoElemento(profile, kolor, largue, location):
    df = pd.read_csv("inventario.csv")
    df.loc[len(df)] = [profile, kolor, largue, location]
    df.to_csv("inventario.csv", index=False)

def borrarElemento(profile, kolor, largue, location):
    df = pd.read_csv("inventario.csv")
    df = df.drop(df[(df.perfil == profile) & (df.color == kolor) & (df.largo == largue) & (df.ubicación == location)].index)
    df.to_csv("inventario.csv", index=False)

def filtrarElementos(profile, kolor, largue, location):
    df = pd.read_csv("inventario.csv")
    if profile != "" or None:
        df = df[df.perfil == profile]
    if kolor != "" or None:
        df = df[df.color == kolor]
    if largue != "" or None:
        if "-" in largue:
            largue = largue.split("-")
            df = df[(df.largo >= float(largue[0])) & (df.largo <= float(largue[1]))]
        else:
            df = df[df.largo == float(largue)]
    if location != "" or None:
        df = df[df.ubicación == location]

    if df.empty:
        return "No se encontraron elementos con esas características."
    else:
        return df

#nuevoElemento("marco - corredera", "blanco", "7.0", "A2")
#print(filtrarElementos("marco - corredera", "caoba", "200-300", "E10"))
