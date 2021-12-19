## Import Library
from flask import Flask,jsonify,request
from bd import ShowData,Mean,Insert,Delete,Edit
from pymongo import MongoClient
app = Flask(__name__)


#Make route

@app.route('/Dictionary')
def ALLdata():
    Words = ShowData()
    return jsonify(Words)

@app.route('/Dictionary/<string:x4>')
def significado(x4):
      Words =  Mean(x4)
      if Words!=None and Words != []:
          return jsonify(Words)
      else:
          return jsonify({"message":'Esta Palabra no Existe en el Diccionario'})

@app.route('/Dictionary',methods=['POST'])
def add():
    x1=request.json['Palabra_E']
    x2= request.json["Palabra_S"]
    Insert(x1,x2)
    Word = ShowData()
    return jsonify({'message ':'Palabra añadida de forma exitosa',"Datos": Word})

@app.route('/Dictionary/<string:Palabra_E>',methods =['PUT'])
def Editar(Palabra_E):
    Word = ShowData()
    if Word !=None and Word != []:
        x5 = request.json['Palabra_E']
        x6= request.json['Palabra_S']
        Edit(x5,x6)
        return jsonify({"message":'Palabra Modificada'})
    else:
        return jsonify({"message":'Palabra no encontrada en el diccionario'})

@app.route('/Dictionary/<string:Palabra_E>',methods=['DELETE'])
def deleteData(Palabra_E):
    Words = ShowData()
    if Words !=None and Words != []:
        x3 = request.json['Palabra_E']
        Delete(x3)
        Words = ShowData()
        return jsonify({"message":'Palabra Eliminada',"Datos ":Words})
    else:
        return jsonify({"message":'Palabra No encontrada'})

if __name__ == '__main__':
    app.run(debug=True,port=5000)