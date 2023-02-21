from pymongo import MongoClient
import certifi 

ca = certifi.where()

client = MongoClient('mongodb+srv://sparta:test@cluster0.d4m39ds.mongodb.net/?retryWrites=true&w=majority', tlsCAFile = ca)
db = client.dbsparta





db.movies.update_one({'title':'가버나움'},{'$set':{'star':0}})