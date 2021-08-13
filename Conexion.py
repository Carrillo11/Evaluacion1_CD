import pymongo

client = pymongo.MongoClient("mongodb+srv://Rene:cg1527@renecluster.lhkqe.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test

print(client.list_database_names())