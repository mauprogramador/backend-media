from app.domain.usecases.video import RemoveVideo
from app.data.protocols.video import (
    RemoveVideoRepository,
    DeleteVideoRepository
)


class DbRemoveVideo(RemoveVideo):
    def __init__(
        self,
        remove_video_repository: RemoveVideoRepository,
        delete_video_repository: DeleteVideoRepository
    ) -> None:
        self.__remove_video_repository = remove_video_repository
        self.__delete_video_repository = delete_video_repository

    async def remove_video(self, data: RemoveVideo.Input) -> None:
        blob = await self.__remove_video_repository.remove_video(data)
        self.__delete_video_repository.delete_video(blob)
