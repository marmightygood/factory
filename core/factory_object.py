import uuid

class factory_object:
    #an id that identifies each object
    factory_scoped_id = str(uuid.uuid4())

    #class fields that can be used to construct a version of this class from a file
    config_fields = dict()

