from app.domain.usecases.photo import UploadPhoto
from app.data.protocols.photo import (
    ImageProcessingRepository,
    UploadImageRepository,
    InsertPhotoRepository
)


class DbUploadPhoto(UploadPhoto):
    def __init__(
        self,
        image_processing_repository: ImageProcessingRepository,
        upload_image_repository: UploadImageRepository,
        insert_photo_repository: InsertPhotoRepository
    ) -> None:
        self.__image_processing_repository = image_processing_repository
        self.__upload_image_repository = upload_image_repository
        self.__insert_photo_repository = insert_photo_repository

    async def upload_photo(self, data: UploadPhoto.Input) -> None:
        image = self.__image_processing_repository.handle(data.file)

        upload_data = UploadImageRepository.Input(image=image, uuid=data.uuid)
        insert_data = self.__upload_image_repository.upload_image(upload_data)

        await self.__insert_photo_repository.insert_photo(insert_data)
