#Importamos la libreria pymongo

from pymongo import MongoClient

cliente= MongoClient("localhost")

#Creamos la base de datos haciendo uso de la libreria antes importada
db= cliente["DiccionarioMongoDB"]

basedatos = db['Diccionario']

# Funciones para la manipulación de la base de datos.

def Insert(x1,x2):
    basedatos.insert_one(({'Palabra_E':x1,
                        'Palabra_S':x2}))
  
            
def Delete(x3):
    basedatos.delete_one({'Palabra_E': x3})

def ShowData():
    Datos = []
    for datos in basedatos.find({}):
        diccionary = {}
        diccionary['Palabra_E'] = datos['Palabra_E']
        diccionary['Palabra_S'] = datos['Palabra_S']
        Datos.append(diccionary)
    return Datos
        
def Mean(x4):
    Datos = []
    for datos in basedatos.find({'Palabra_E':x4}):
        diccionary = {}
        diccionary['Palabra_E'] = datos['Palabra_E']
        diccionary['Palabra_S'] = datos['Palabra_S']
        Datos.append(diccionary)
    return Datos

def Edit(x5,x6):
    basedatos.update_one({'Palabra_E': x5},
                         {"$set": {"Palabra_S":x6}})
