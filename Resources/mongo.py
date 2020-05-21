import json
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client.avocado

with open('./avocado.json', 'r') as f:
    data = json.load(f)
    
f.close()

with open('./cleaned_wine.json', 'r') as g:
    wine_data = json.load(g)

g.close()

db.avocado_col.insert_many(data)

db.wine_col.insert_many(wine_data)

