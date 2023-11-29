import firebase_admin
from firebase_admin import credentials, firestore, storage
from google.cloud.firestore_v1.client import Client


class FirebaseApi:
    def __init__(self) -> None:
        self.cred = credentials.Certificate("private_key.json")
        self.app = firebase_admin.initialize_app(self.cred)
        self.client: Client = firestore.client(self.app)
        self.bucket = storage.bucket("snapcut-371a5.appspot.com")

    def upload(self):
        blob = self.bucket.blob("data.txt")
        blob.upload_from_filename("data.txt")
        blob.make_public()
        return blob.public_url



from pymongo.mongo_client import MongoClient
from .env import MONGODB_URI, DATABASE, COLLECTION
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
