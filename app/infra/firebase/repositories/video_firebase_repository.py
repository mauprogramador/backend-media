from app.utils.uuid_faker import hash_uuid, generate_uuid
from app.infra.firebase import FirebaseService
from tempfile import TemporaryDirectory
from app.data.protocols.video import (
    UploadVideoRepository,
    InsertVideoRepository,
    DeleteVideoRepository
)
from os.path import join


class VideoFirebaseRepository(
    UploadVideoRepository,
    DeleteVideoRepository
):
    MODE = "wb"
    BLOB = "videos"
    EXTENSION = ".webm"
    CONTENT_TYPE = "video/webm"

    def __init__(
        self,
        firebase_service: FirebaseService
    ) -> None:
        self.__firebase_service = firebase_service

    def upload_video(self, data: UploadVideoRepository.Input) -> InsertVideoRepository.Input:
        uuid = generate_uuid(data.uuid)
        filename = uuid + self.EXTENSION

        with TemporaryDirectory() as dir:
            file_path = join(dir, filename)
            blob_path = join(self.BLOB, hash_uuid(data.uuid), filename)

            with open(file_path, self.MODE) as file:
                file.write(data.video)

            firebase_data = FirebaseService.Input(
                content_type=self.CONTENT_TYPE,
                blob_path=blob_path,
                file_path=file_path
            )
            public_url = self.__firebase_service.upload(firebase_data)

            return UploadVideoRepository.Output(
                user_uuid=data.uuid,
                video_uuid=uuid,
                url=public_url,
                blob=blob_path
            )

    def delete_video(self, blob_path: str) -> None:
        self.__firebase_service.delete_blob(blob_path)
