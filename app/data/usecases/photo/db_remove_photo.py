from app.domain.usecases.photo import RemovePhoto
from app.data.protocols.photo import (
    DeleteImageRepository,
    RemovePhotoRepository
)


class DbRemovePhoto(RemovePhoto):
    def __init__(
        self,
        remove_photo_repository: RemovePhotoRepository,
        delete_image_repository: DeleteImageRepository
    ) -> None:
        self.__remove_photo_repository = remove_photo_repository
        self.__delete_image_repository = delete_image_repository

    async def remove_photo(self, uuid: str) -> None:
        blob = await self.__remove_photo_repository.remove_photo(uuid)
        self.__delete_image_repository.delete_image(blob)
