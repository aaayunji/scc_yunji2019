from pymongo import MongoClient
client = MongoClient('localhost',27017)
db = client.dbsparta

def save(genreList, title, directorList, castList):
    collection.save("genre":genreList,"title":title,"director":directorList,"cast":castList)
