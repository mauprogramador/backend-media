from pymongo.mongo_client import MongoClient
from app.main.config.env import MONGODB_URI, DATABASE, COLLECTION
from app.utils.logger import Logger


class MongoConnection:
    def __init__(self):
        pass

    def __enter__(self):
        self.client = MongoClient(MONGODB_URI)
        try:
            self.client.admin.command('ping')

        except Exception:
            self.client.close()
            message = "Cannot connect to MongoDB"
            Logger.error(message)
            raise ConnectionError(message)

        database = self.client.get_database(DATABASE)
        collection = database.get_collection(COLLECTION)

        return collection

    def __exit__(self, exc_type, exc_value, traceback):
        self.client.close()
