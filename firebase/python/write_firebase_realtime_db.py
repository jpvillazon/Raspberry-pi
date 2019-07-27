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

data = {“numerico”: 80, “texto”:”Texto de prueba“, “decimales”: 123.45,”logico”: False}
db.child(“database”).set(data)
db.child(“database”).push(data)

data = {“numerico”: 10, “texto”:”Texto de prueba modificado“, “decimales”: 543.21,”logico”: True}
db.child(“database”).update(data)
