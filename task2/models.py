import certifi
from mongoengine import *


uri = "mongodb+srv://hw08:567234@pythonweb.5mdxxbn.mongodb.net/hw8?retryWrites=true&w=majority"
connection = connect(host=uri,  tlsCAFile=certifi.where(), ssl=True)


class Contact(Document):
    name = StringField(required=True)
    email = StringField(required=True)
    send_email = BooleanField(default=False)
