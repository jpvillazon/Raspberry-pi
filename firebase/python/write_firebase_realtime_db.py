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

data = {"integer": 80, "string":"Test String", "float": 123.45,"bool": False}
db.child("database").set(data)
db.child("database").push(data)

data = {"integer": 10, "string":"Test String Updated", "float": 543.21,"bool": True}
db.child("database").update(data)
