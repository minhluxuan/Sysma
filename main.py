import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")

#Khởi tạo một database có tên là mydb
db = client["mydb"]

#Khởi tạo một collection có tên là myCollection
col = db["myCollection"]

#insert dữ liệu vào collection
"""
dict = [{"name":"Minh","age":"18"},
        {"name":"Tâm","age":"18"},
        {"name":"Huy","age":"18"},
        {"name":"Nhân","age":"18"}
        ]

col.insert_many(dict)
"""

#In dữ liệu ra màn hình
"""
x = col.find()
for data in x:
    print(data)

"""

#Tìm dữ liệu có điều kiện: VD: tìm tất cả document có tên Minh

"""
myquery = {"age":"18"}

x = col.find(myquery)
for data in x:
    print(data)
"""

#Sắp xếp dữ liệu
"""
x = col.find().sort("name",-1)
for data in x:
    print(data)
"""

#Update dữ liệu
"""
inserted_data = {"name":"Minh"}
myquery = {"$set":{"name":"A"}}

col.update_many(inserted_data,myquery)

for data in col.find():
    print(data)
"""

#Xóa dữ liệu
"""
myquery = {"name":"A"}

col.delete_many(myquery)
for data in col.find():
    print(data)

"""

col.drop()









