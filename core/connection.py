from core import factory_object as f
import sqlalchemy
import uuid


class connection(f.factory_object):

    def __init__(self, db_url, factory_scoped_id):
        self.db_url = db_url
        self.engine = None
        self.connection = None
        self.factory_scoped_id = factory_scoped_id

    def connect(self):
        self.engine = sqlalchemy.create_engine(self.db_url)
        self.connection = self.engine.connect()


class new_connection():
    
    def __init__(self, db_url):

        factory_scoped_id = str(uuid.uuid4())
        connection = connection(db_url, factory_scoped_id)
        return connection

