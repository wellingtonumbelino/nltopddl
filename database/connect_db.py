from pymongo import MongoClient

hostname = "localhost"
port = 27017
client = MongoClient(hostname, port)
db = client.nltopddl
nl_collection = db.nl_examples
pddl_collection = db.pddl_examples

def return_all_nl_examples():
  return nl_collection.find()

def return_pddl_example(pddl_id):
  return pddl_collection.find_one({ "pddl_id": pddl_id })['code_example']

def close_connection():
  client.close()