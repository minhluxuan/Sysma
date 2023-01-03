import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")

db = client["aiot"]
dayRange = db["day_range"]

list = [{"name":"Minh Lu Xuan", "age":"18"},
		{"name":"Tam", "age":"18"},
		{"name":"Huy", "age":"18"},
		{"name":"Nhan", "age":"18"},
		{"name":"Khiem", "age":"18"}
		]

for x in dayRange.find():
	print(x)

#data = dayRange.insert_many(list)

#dayRange.delete_many({})

