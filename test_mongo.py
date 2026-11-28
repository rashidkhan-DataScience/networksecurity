from pymongo import MongoClient
uri = "mongodb+srv://rashid:Admin%40123@networksecurity.fokgaqi.mongodb.net/"
client = MongoClient(uri)
try:
    client.admin.command("ping")
    print("Connected successfully")
    client.close()

except Exception as e:
    raise Exception(
        "The following error occurred: ", e)