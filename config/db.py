import os
from pymongo import MongoClient

conn = MongoClient(os.environ['MONGO_CONN'])
