from app.infra.mongo.database import MongoConnection
from app.infra.mongo import PHOTO_PROJECTION
from app.domain.models import PhotoModelOut
from app.data.protocols.photo import (
    InsertPhotoRepository,
    RemovePhotoRepository
)
from app.models import PhotoDocument
from app.main.exceptions import (
    InternalError,
    NotFound
)
from bson import ObjectId


class PhotoMongoRepository(
    InsertPhotoRepository,
    RemovePhotoRepository
):
    KEY = "photo"

    async def insert_photo(self, data: InsertPhotoRepository.Input) -> None:
        photo_document = PhotoDocument(url=data.url, blob=data.blob)
        photo_update = {"$set": {self.KEY: photo_document.model_dump()}}
        with MongoConnection() as collection:
            result = collection.update_one({"_id": ObjectId(data.uuid)}, photo_update)
            if result.matched_count == 0:
                raise NotFound("User")
            if result.matched_count == 1 and result.modified_count == 0:
                raise InternalError("Error in updating photo")

    async def remove_photo(self, uuid: str) -> str:
        photo_update = {"$set": {self.KEY: None}}
        with MongoConnection() as collection:
            result = collection.find_one({"_id": ObjectId(uuid)}, PHOTO_PROJECTION)
            if not result:
                raise NotFound("User")
            if not result[self.KEY]:
                raise NotFound("Photo")
            photo = PhotoModelOut(**result[self.KEY])
            result = collection.update_one({"_id": ObjectId(uuid)}, photo_update)
            if result.matched_count == 0:
                raise NotFound("User")
            if result.matched_count == 1 and result.modified_count == 0:
                raise InternalError("Error in updating photo")
            return photo.blob
