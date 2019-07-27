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
    print(message["event"])
    print(message["path"])
    print(message["data"])

try:
    my_stream = db.child(“database”).stream(stream_handler)
except KeyboardInterrupt:
    my_stream.close()
    sys.exit()
