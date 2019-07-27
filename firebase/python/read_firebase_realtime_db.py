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

data_bool=db.child("database/bool").get()
data_integer=db.child("database/integer").get()
data_string=db.child("database/string").get()
data_float=db.child("database/float").get()

print "Bool : ",data_bool.val()
print "Integer : ", data_integer.val()
print "String : ", data_string.val()
print "Float: ", data_float.val()

db.child("database").child("string").remove()
db.child("database").remove()
