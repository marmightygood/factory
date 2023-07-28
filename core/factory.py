from core import factory_object as f
import json

class factory(f.factory_object):

    pipelines = dict()
    connections = dict()
    datasets = dict()
   
    def __init__(self):
        print ("Started factory")

    def load(self, factory_file):
        with open(factory_file, "r") as file:
            self.data = json.load(file)
        self.name = self.data["name"]
        return self.name

    def unload(self, factory_file):
        print ("Not implemented")        

    def get_connections(self):
        return self.data.get("connections", {})

    def get_datasets(self):
        return self.data.get("datasets", {})

    def get_pipelines(self):
        return self.data.get("pipelines", {})        
    
    def __str__(self):
        return self.name
