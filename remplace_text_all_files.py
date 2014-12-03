import os

FIND="TEXTO QUE QUEREMOS BUSCAR PARA REMPLAZAR"
REMPLACE="LO REMPLAZAMOS POR ESTO"
DIRECTORIO="/home/endikaig/Escritorio/ejemplos/"

def load_file(name):
    f=open(name,'r')
    lineas=f.readlines()
    f.close()
    text=""
    for x in lineas:
        text+=x
    return text

def new_file(name,text):
    f=open(name,'w')
    f.write(text)
    f.close()

def remplace_text(text):
    text_new=text.replace(FIND,REMPLACE)
    if text != text_new:
        return text_new
    else:
        text=text.lower()
        text_new=text.replace(FIND.lower(),REMPLACE.lower())
        if text != text_new:
            return 1
    return 0

def analyze(dire):
    for dirname, dirnames, filenames in os.walk(dire):
        for subdirname in dirnames:
            new_dire=str(os.path.join(dirname, subdirname)+"/")
            print new_dire
            analyze(new_dire)

        for filename in filenames:
            filename=str(dire+filename)
            valor=load_file(filename)
            valor=remplace_text(valor)
            if str(valor)=='1':            
                print("Por seguridad remplaza el texto manualmente en el fichero %s"%(filename))
            elif str(valor)!='0':
                new_file(filename,valor)
                print("Remplazado correctamente en el fichero %s"%(filename))

analyze(DIRECTORIO)
