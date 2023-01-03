import pymongo as pmg

#connect client with mongo server
client = pmg.MongoClient('localhost', 27017)

#create a database
db = client["mydatabase"]

#create a collection (table)
collection = db["collection"]

#create a dataset like a dictionary

dict = [{"name":"Huy", "age":"18"},
        {"name":"Huy", "age":"18"},
        {"name":"Minh", "age":"18"}]



#insert data to collection
#data = collection.insert_many(dict)

#find all inserted data
#for inserted_data in collection.find():
#    print(inserted_data)

"""
myquery = {"age":"18"}

for dt in collection.find(myquery):
    print(dt)
"""


"""
docs = collection.find().sort("name",-1)
for dt in docs:
    print(dt)
"""
#delete a document

"""
myquery = {"name":"Huy"}

collection.delete_many(myquery)

for dt in collection.find():
    print(dt)
"""

myquery = {"name":"Minh"}

update_data = {"$set":{"name":"Khiêm"}}

collection.update_many(myquery,update_data)
for data in collection.find().limit(2):
     print(data)







