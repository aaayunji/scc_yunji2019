from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# db.users.insert_one({'name':'bobby','age':21})
#
# db.users.insert_one({'name':'kay','age':27})
# db.users.insert_one({'name':'john','age':30})


all_users = db.users.find()

print(all_users[0])
print(all_users[0]['name'])

for user in all_users :
    print(user)

user = db.users.find_one({'name':'bobby'})
print (user)

user = db.users.find_one({'name':'bobby'},{'_id':0})
print (user)

db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

user = db.users.find_one({'name':'bobby'})
print (user)

