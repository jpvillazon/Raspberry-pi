import pyrebase

config = {
  "apiKey": "",
  "authDomain": "",
  "databaseURL": "",
  "projectId": "",
  "storageBucket": "",
  "messagingSenderId": "",
  "appId": ""
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

salida_logico=db.child("database/logico").get()
salida_numerico=db.child("database/numerico").get()
salida_texto=db.child("database/texto").get()
salida_decimal=db.child("database/decimal”).get()

print "salida logico: ",salida_logico.val()
print "salida numerico: ", salida_numerico.val()
print "salida texto: ", salida_texto.val()
print "salida decimal: ", salida_decimal.val()

db.child(“database”).child(“texto”).remove()
db.child(“database”).remove()
