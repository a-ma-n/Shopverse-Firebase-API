import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import firestore
import urllib.request
import cv2
import numpy as np
cred = credentials.Certificate("firebase.json")
firebase_admin.initialize_app(cred,
                                  { "databaseURL":
                                        "https://test-c418a-default-rtdb.firebaseio.com"})

db2 = firestore.client()
imgs=[]

def query():
    doc_ref = db2.collection(u'aman').document(u'photos')
    doc = doc_ref.get()
    k=[]
    if doc.exists:
        k=doc.to_dict().values()
        k=list(k)
    return k

def url_to_image (url):
    resp = urllib.request.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image

for i in query():
    imgs.append(url_to_image (i))
print(len(imgs))