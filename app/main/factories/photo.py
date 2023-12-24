from app.infra.firebase.repositories import PhotoFirebaseRepository
from app.data.usecases.photo import DbUploadPhoto, DbRemovePhoto
from app.infra.mongo.repositories import PhotoMongoRepository
from app.infra.firebase import FirebaseService
from app.usecases import ImageProcessing


def make_db_upload_photo() -> DbUploadPhoto:
    image_processing = ImageProcessing()
    firebase_service = FirebaseService()
    photo_firebase_repository = PhotoFirebaseRepository(firebase_service)
    photo_mongo_repository = PhotoMongoRepository()

    return DbUploadPhoto(
        image_processing,
        photo_firebase_repository,
        photo_mongo_repository
    )


def make_db_remove_photo() -> DbRemovePhoto:
    photo_mongo_repository = PhotoMongoRepository()
    firebase_service = FirebaseService()
    photo_firebase_repository = PhotoFirebaseRepository(firebase_service)

    return DbRemovePhoto(
        photo_mongo_repository,
        photo_firebase_repository
    )
