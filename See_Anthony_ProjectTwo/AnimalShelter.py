from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    def __init__(self, username=None, password=None):
        self.client = MongoClient('mongodb://%s:%s@localhost:47425/AAC' % (username, password))
        self.database = self.client['AAC']

    def create(self, data):
        if data is not None:
            data_insert = self.database.animals.insert(data)
            if data_insert != 0:
                return True
                print("True")
            else:
                return False
                print("False")
        else:
            raise Exception("Nothing to save. Data parameters are empty")

    def read(self, search=None):
        if search:
            data = self.database.animals.find(search, {"_id":False})
        else:
            data = self.database.animals.find({},{"_id":False})
        return data

    def update(self, search=None, data=None):
        if data is not None:
            if search is not None:
                result = self.database.animals.update_many(search, {"$set":data})
                return True
            else:
                print("Search was not found, or there were no parameters")
                return False
        else:
            return False
            print("Data to edit contained nothing")

    def delete(self, search=None):
        if search is not None:
            self.database.animals.remove(search)
            return True
        else:
            return False
            print("Search parameter was false")
            
        
