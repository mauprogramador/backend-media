from app.infra.firebase import FirebaseService
from app.utils.uuid_faker import hash_uuid
from tempfile import TemporaryDirectory
from app.data.protocols.photo import (
    UploadImageRepository,
    DeleteImageRepository
)
from os.path import join


class PhotoFirebaseRepository(
    UploadImageRepository,
    DeleteImageRepository
):
    BLOB = "images"
    FORMAT = "WEBP"
    EXTENSION = ".webp"
    CONTENT_TYPE = "image/webp"

    def __init__(
        self,
        firebase_service: FirebaseService
    ) -> None:
        self.__firebase_service = firebase_service

    def upload_image(self, data: UploadImageRepository.Input) -> UploadImageRepository.Output:
        filename = hash_uuid(data.uuid) + self.EXTENSION

        with TemporaryDirectory() as dir:
            file_path = join(dir, filename)
            data.image.save(file_path, self.FORMAT)
            blob_path = join(self.BLOB, filename)

            firebase_data = FirebaseService.Input(
                content_type=self.CONTENT_TYPE,
                blob_path=blob_path,
                file_path=file_path
            )
            public_url = self.__firebase_service.upload(firebase_data)

            return UploadImageRepository.Output(
                uuid=data.uuid,
                url=public_url,
                blob=blob_path
            )

    def delete_image(self, blob_path: str) -> None:
        self.__firebase_service.delete(blob_path)
