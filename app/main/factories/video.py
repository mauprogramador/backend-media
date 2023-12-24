from app.infra.firebase.repositories import VideoFirebaseRepository
from app.data.usecases.video import DbUploadVideo, DbRemoveVideo
from app.infra.mongo.repositories import VideoMongoRepository
from app.infra.firebase import FirebaseService
from app.usecases import VideoProcessing


def make_db_upload_video() -> DbUploadVideo:
    video_processing = VideoProcessing()
    firebase_service = FirebaseService()
    video_firebase_repository = VideoFirebaseRepository(firebase_service)
    video_mongo_repository = VideoMongoRepository()

    return DbUploadVideo(
        video_processing,
        video_firebase_repository,
        video_mongo_repository
    )


def make_db_remove_video() -> DbRemoveVideo:
    video_mongo_repository = VideoMongoRepository()
    firebase_service = FirebaseService()
    video_firebase_repository = VideoFirebaseRepository(firebase_service)

    return DbRemoveVideo(
        video_mongo_repository,
        video_firebase_repository
    )
