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

def stream_handler(message):
    if message["data"]== True and message["path"] == "/quit":
      print "Quitting"
      quit()
      
    print(message["event"])
    print(message["path"])
    print(message["data"])
    

my_stream = db.child("database").stream(stream_handler)
#my_stream.close()
