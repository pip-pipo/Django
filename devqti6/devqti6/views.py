import pyrebase
from django.shortcuts import render
Config = {
    'apiKey': "AIzaSyC_jlWEyEZAx289R8qzKZK0xTDBUYuDIn4",
    'authDomain': "djangoapp-8bca1.firebaseapp.com",
    'databaseURL': "https://djangoapp-8bca1.firebaseio.com",
    'projectId': "djangoapp-8bca1",
    'storageBucket': "djangoapp-8bca1.appspot.com",
    '  messagingSenderId': "457469915103",
    '  appId': "1:457469915103:web:16bd2d85651ac470371e6a",
    'measurementId': "G-WM7BBTW0ZW"
}


# initialize app with config
firebase = pyrebase.initialize_app(config)

# authenticate a user
auth = firebase.auth()
user = auth.sign_in_with_email_and_password(
    "email@usedforauthentication.com", "FstrongPasswordHere")


db = firebase.database()
