from app.main.exceptions import FailedDependency, NotFound
from app.main.config import FIREBASE_KEY, FIREBASE_BUCKET
from firebase_admin.credentials import Certificate
from firebase_admin.storage import bucket
from firebase_admin import initialize_app
from app.data.protocols.firebase import (
    UploadRepository,
    DeleteRepository,
    DeleteBlobRepository
)
from google.cloud.storage import Bucket
from app.utils.logger import Logger
from os.path import dirname


class FirebaseService(
    UploadRepository,
    DeleteRepository,
    DeleteBlobRepository
):
    BUCKET: Bucket = None

    @classmethod
    def load_bucket(cls):
        try:
            cred = Certificate(FIREBASE_KEY)
            app = initialize_app(cred)
            firebucket = bucket(FIREBASE_BUCKET, app)
        except Exception:
            message = "Cannot validate firebase credentials"
            Logger.error(message)
            raise ValueError(message)
        if not firebucket.exists():
            raise ConnectionError("Cannot find firebase bucket")
        cls.BUCKET = firebucket

    def upload(self, data: UploadRepository.Input) -> str:
        try:
            blob = self.BUCKET.blob(data.blob_path)
            blob.upload_from_filename(data.file_path, data.content_type)
            blob.make_public()

            return blob.public_url

        except Exception:
            raise FailedDependency("Error in uploading blob")

    def delete(self, blob_path: str) -> None:
        try:
            blob = self.BUCKET.blob(blob_path)
            if not blob.exists():
                raise NotFound("Blob")
            blob.delete()
        except Exception:
            raise FailedDependency("Error in deleting blob")

    def delete_blob(self, blob_path: str) -> None:
        try:
            blob = self.BUCKET.blob(blob_path)
            if not blob.exists():
                raise NotFound("Blob")
            blob.delete()
            folder = dirname(blob_path) + "/"
            blobs = self.BUCKET.list_blobs(prefix=folder)
            if len(list(blobs)) == 1:
                blob = self.BUCKET.blob(folder)
                if not blob.exists():
                    raise NotFound("Blob")
                blob.delete()
        except Exception:
            raise FailedDependency("Error in deleting blob")
