import os
import pickle

file = "./students.data"

class Database:
    
    @staticmethod
    def initialize():
        if not(os.path.exists(file)):
            handler = open(file,'wb')
            pickle.dump([],handler)
            handler.close
            
    @staticmethod
    def save(data):
        with open(file,'wb') as handler:
            pickle.dump(data,handler)
            handler.close
            
    @staticmethod
    def read():
        with open(file,'rb') as handler:
            data = pickle.load(handler)
        handler.close
        return data