import pprint
import pymongo
from pymongo import MongoClient

def pp(obj):
    pprint.pprint(obj)
    
def ppall(col):
    for p in col:
        pp(p)

client = MongoClient()
database = client["TwitterDB"]
collection = database["tweets"]

# Query 1
def query1():
    distinct_users = collection.distinct("user")
    pp(len(distinct_users))

# Query 2
def query2():
    pipeline = [
        {
            '$match': {
                'text': {
                    '$regex': '@\w+'
                }
            }
        }, 
        {
            '$group': {
                '_id': '$user',
                'references': {
                    '$sum': 1
                }
            }
        }, 
        {
            '$sort': {
                'references': -1
            }
        }, 
        {
            '$limit': 10.0
        }
    ]

    results = collection.aggregate(pipeline)

    for item in results:
    	print(item)

#Query 3
def query3():
    pipeline = [
        {
            '$addFields': {
                'words': {
                    '$split': ['$text', ' ']
                }
            }
        },
        {
            '$unwind': '$words'
        }, 
        { 
            '$match': {
                'words': {
                    '$regex':'@\w+','$options': 'm'
                }
            }
        }, 
        {
            '$group': {
                '_id':'$words',
                'total': {
                    '$sum': 1
                }
            }
        },
        {
            '$sort': {
                'total': -1
            }
        },
        {
            '$limit': 5
        }
    ]

    results = collection.aggregate(pipeline)

    for item in results:
        print(item)

#Query 4
def query4():
    pipeline = [
        {
            '$group':{
                '_id':'$user',
                'count':{
                    '$sum':1
                }
            }
        },
        {
            '$sort':{
                'count': -1
            }
        },
        {
            '$limit': 10
        }
    ]
    results = collection.aggregate(pipeline)

    for item in results:
        print(item)

#Query 5
def query5():
    pipeline=[
        {
            '$facet':
                {
                    'grumpy': [
                            {
                                '$match': {
                                    'polarity': {
                                            '$eq':0
                                    }
                                }
                            },
                            {
                                '$group': {
                                    '_id' : '$user',
                                    'count' : {
                                        '$sum' : 1
                                    }
                                }
                            },
                            {
                                '$sort': {
                                    'count': -1
                                }
                            },
                            {
                                '$limit': 5
                            }
                    ],
                    'happy':[
                        {
                            '$match':{
                                'polarity':{
                                        '$eq':4
                                }
                            }
                        },
                        {
                            '$group':{
                                '_id' : '$user',
                                'count' : {
                                    '$sum' : 1
                                }
                            }
                        },
                        {
                            '$sort':{
                                'count': -1
                            }
                        },
                        {
                            '$limit': 5
                        }
                    ]
                }
        }
    ]
    results = collection.aggregate(pipeline)

    for item in results:
        print(item)

print("Total users:")
query1()
print("Users who link the most to others:")
query2()
print("Most mentioned users:")
query3()
print("Most active users:")
query4()
print("Most grumpy and most happy:")
query5()