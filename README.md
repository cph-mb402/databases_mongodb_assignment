To run this project make sure you have your database mapped to the default port (27017) and the csv data imported into the db as TwitterDB.tweets, have python3 installed, and have the used modules installed with pip3. Might work on python2 as well, but I have not tested it on that version. When you are sure all those are done just run the assignment.py file.

You can use these 2 commands to launch a mongodb locally through docker:
```
docker run --rm --publish=27017:27017 --name dbms -d mongo:latest
```
```
docker run --rm -v $(pwd)/data:/data/db --publish=27017:27017 --name dbms -d mongo:latest
```


Running it in the console this is the response I get:
```
➜  mongo_db_assignment git:(master) python3 assignment.py

Total users:
Result :  659774

Users who link the most to others:
{'_id': 'lost_dog', 'links': 549}
{'_id': 'tweetpet', 'links': 310}
{'_id': 'VioletsCRUK', 'links': 251}
{'_id': 'what_bugs_u', 'links': 246}
{'_id': 'tsarnick', 'links': 245}
{'_id': 'SallytheShizzle', 'links': 229}
{'_id': 'mcraddictal', 'links': 217}
{'_id': 'Karen230683', 'links': 216}
{'_id': 'keza34', 'links': 211}
{'_id': 'TraceyHewins', 'links': 202}

Most mentioned users:
('@mileycyrus', 4499)
('@tommcfly', 3886)
('@ddlovato', 3466)
('@DavidArchie', 1298)
('@Jonasbrothers', 1286)

Most active users:
{'_id': 'lost_dog', 'count': 549}
{'_id': 'webwoke', 'count': 345}
{'_id': 'tweetpet', 'count': 310}
{'_id': 'SallytheShizzle', 'count': 281}
{'_id': 'VioletsCRUK', 'count': 279}
{'_id': 'mcraddictal', 'count': 276}
{'_id': 'tsarnick', 'count': 248}
{'_id': 'what_bugs_u', 'count': 246}
{'_id': 'Karen230683', 'count': 238}
{'_id': 'DarkPiano', 'count': 236}

Most grumpy and most happy:
{
	'grumpy': [
		{'_id': 'lost_dog', 'count': 549},
        {'_id': 'tweetpet', 'count': 310},
        {'_id': 'webwoke', 'count': 264},
        {'_id': 'mcraddictal', 'count': 210},
        {'_id': 'wowlew', 'count': 210}
    ],
 	'happy': [
 		{'_id': 'what_bugs_u', 'count': 246},
        {'_id': 'DarkPiano', 'count': 231},
        {'_id': 'VioletsCRUK', 'count': 218},
        {'_id': 'tsarnick', 'count': 212},
        {'_id': 'keza34', 'count': 211}
    ]
}
```


Model | Atomicity | Sharding |Indexes |Large Number of Collections | Collection Contains Large Number of Small Documents
----|:----:|:----:|:----:|:----:|:----:
Arrays of Ancestors	|x| |x|x| |
Materialized paths  | |x ||x|x|
Nested sets			|x|x|x|| |

Arrays of Ancestors:

Atomicity: Writing is atomic because the data is inserted into a single document, and the relations are specified in the inserted object, so no need to insert/update other objects

Indexes: Ancestors and descendants can be quickly found by creating an index on the elements of the ancestors field

Large number of collections: Viable strategy, reducing the number of documents in each collection, therefore improving performance, since all ancestors are stored in each document

Materialized paths:

Sharding: Since the pattern is fast and straightforward, sharding should be implemented as a last resort

Large Number of Collections: Viable strategy, reducing the number of documents in each collection, therefore improving performance and possibly keeping document size smaller

Collection Contains Large Number of Small Documents: In the case there are a lot of documents with a small path, and they are often accessed as a group, rolling up might be a good solution

Nested Sets:

Atomicity: Writing is atomic because the data is inserted into a single document, and the relations are specified in the inserted object, so no need to insert/update other objects

Sharding: Since this pattern is not so good at modifying the tree structure, it might benefit from sharding, but it might also increase complexity too much

Collection Contains Large Number of Small Documents: This pattern could benefit from rolling up if the same group of objects is constalty retrieved

