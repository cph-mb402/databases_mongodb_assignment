import pprint
import pymongo
from pymongo import MongoClient
from bson.regex import Regex
from bson.son import SON

def pp(obj):
    pprint.pprint(obj)
    
def ppall(col):
    for p in col:
        pp(p)

client = MongoClient()
database = client["twitter"]
collection = database["tweets"]

# Users Number
distinct_users = collection.distinct("user")
pp(len(distinct_users))

# Top 10
pipeline = [
    {
        u"$match": {
            u"text": {
                u"$regex": u"@\\w+"
            }
        }
    }, 
    {
        u"$group": {
            u"_id": u"$user",
            u"references": {
                u"$sum": 1.0
            }
        }
    }, 
    {
        u"$sort": SON([ (u"references", -1) ])
    }, 
    {
        u"$limit": 10.0
    }
]

retweets = collection.aggregate(
    pipeline, 
    allowDiskUse = False
)

for doc in retweets:
	print(doc)

# while (retweets.hasNext()): 
   # print(tojson(retweets.next()));