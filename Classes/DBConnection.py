import pymongo
from Data.Token import TokenDiscord

tokenDiscord = TokenDiscord()

class Connection:

    def __init__(self):
        self.client = pymongo.MongoClient(tokenDiscord.uploadToken()['database'])
        self.collections = self.client.BalleBot['Pontos']

    def get_collection(self):
        return self.collections