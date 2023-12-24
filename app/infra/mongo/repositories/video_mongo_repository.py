from app.infra.mongo.database import MongoConnection
from app.domain.models import VideoModelOut
from app.data.protocols.video import (
    InsertVideoRepository,
    RemoveVideoRepository
)
from app.models import VideoDocument
from app.main.exceptions import (
    InternalError,
    NotFound
)
from bson import ObjectId


class VideoMongoRepository(
    InsertVideoRepository,
    RemoveVideoRepository
):
    KEY = "videos"

    async def insert_video(self, data: InsertVideoRepository.Input) -> None:
        video_document = VideoDocument(**data.model_dump()).model_dump()
        video_update = {"$push": {self.KEY: video_document}}
        with MongoConnection() as collection:
            result = collection.update_one({"_id": ObjectId(data.user_uuid)}, video_update)
            if result.matched_count == 0:
                raise NotFound("User")
            if result.matched_count == 1 and result.modified_count == 0:
                raise InternalError("Error in adding friend")

    async def remove_video(self, data: RemoveVideoRepository.Input) -> str:
        video_find = {"$elemMatch": {"uuid": data.video_uuid}}
        video_update = {"$pull": {self.KEY: {"uuid": data.video_uuid}}}
        with MongoConnection() as collection:
            result = collection.find_one({
                "_id": ObjectId(data.user_uuid),
                self.KEY: video_find
            })
            if not result:
                raise NotFound("Video")
            video = VideoModelOut(**result[self.KEY][0])
            result = collection.update_one({"_id": ObjectId(data.user_uuid)}, video_update)
            if result.matched_count == 0:
                raise NotFound("User")
            if result.matched_count == 1 and result.modified_count == 0:
                raise InternalError("Error in removing video")
            return video.blob
