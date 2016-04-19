from couchdb.mapping import (
    Document, TextField, FloatField, DictField, BooleanField
)

class ModuleTypeModel(Document):
    name = TextField()
    description = TextField()
    class_path = TextField()
    parameters = DictField()
    inputs = DictField()
    outputs = DictField()
    endpoints = DictField()
    procedures = DictField()

class ModuleModel(Document):
    name = TextField()
    type = TextField()
    parameters = DictField()

class ModuleConnectionModel(Document):
    output_module = TextField()
    output_name = TextField()
    input_module = TextField()
    input_name = TextField()

class EnvironmentModel(Document):
    variables = ListField(TextField())

class EnvironmentalDataPointModel(Document):
    environment = TextField()
    variable = TextField()
    is_desired = BooleanField()
    value = FloatField()
    timestamp = FloatField()