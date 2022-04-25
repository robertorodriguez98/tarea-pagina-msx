import json
def LeerLibreria(fichero):
    try:
        f=open(fichero)
        datos = json.load(f)
        f.close
        return datos
    except:
        print("error al leer el fichero")