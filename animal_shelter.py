from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username=None, password=None):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # self.client = MongoClient('mongodb://localhost:27017')
        self.client = MongoClient('mongodb://%s:%s@localhost:29993/?authMechanism=DEFAULT&authSource=AAC'%(username, password))
        # where xxxx is your unique port number
        self.database = self.client['AAC']

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            insert = self.database.animals.insert(data)
            print("Task Finished")# data should be dictionary
            if insert !=0:
                return True            
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD.
    def read(self, data):
        if data is not None:
            data = self.database.animals.find(data, {'_id':False})  # data should be dictionary
# Defaults to findAll method otherwise 
        else:
            data = self.database.animals.findAll()
        
# Finding information, method will show or throw exception
        if data:
            return data        
        else:
            raise Exception("Nothing to search, data parameter is empty") 

# Create method to implement the U in CRUD.
    def update(self, data, param):
        
        if data is not None and type(data) is dict: 
            if param is not None and type(param) is dict:
                # If data and param are dict, then update
                self.database.animals.update_one(data, param)
                # Store update in variable
                animal = self.database.animals.find_one(data)     
            else:
                raise Exception("Nothing to save, parameter is empty")
        else:
            raise Exception("Nothing to save, parameter not type dict")
        return animal
    
# Create method to implement the D in CRUD.
    def drop(self, data):
        
        if data is not None and type(data) is dict: # data should be dictionary 
            print("\nDeleting", data)
            print(self.database.animals.delete_one(data)) 
            print("\nEntry deleted", data)
            
        else:
            raise Exception("Unable to delete entry")
                    