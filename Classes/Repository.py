from Classes.DBConnection import Connection

connection = Connection()

class Repository:

    def __init__(self):
        self.collection = connection.get_collection()

    def insert_one_xp(self, document):
        self.collection.insert_one(document)

    def insert_many_xp(self, documents):
        self.collection.insert_many(documents, True)

    def place_one_xp(self, replacement):
        self.collection.replace_one(filter, replacement, True)

    def update_one_xp(self, value):
        self.collection.update_one({'user_id': value.user_id}, {'$inc': value}, True)

    def update_many_xp(self, update):
        self.collection.update_many(filter, update, True)

    def delete_one_xp(self):
        self.collection.delete_one(filter)

    def delete_many_xp(self):
        self.collection.delete_many(filter)
