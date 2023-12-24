from app.domain.usecases.video import UploadVideo
from app.data.protocols.video import (
    VideoProcessingRepository,
    UploadVideoRepository,
    InsertVideoRepository
)


class DbUploadVideo(UploadVideo):
    def __init__(
        self,
        video_processing_repository: VideoProcessingRepository,
        upload_video_repository: UploadVideoRepository,
        insert_video_repository: InsertVideoRepository
    ) -> None:
        self.__video_processing_repository = video_processing_repository
        self.__upload_video_repository = upload_video_repository
        self.__insert_video_repository = insert_video_repository

    async def upload_video(self, data: UploadVideo.Input) -> None:
        video = self.__video_processing_repository.handle(data.file)

        upload_data = UploadVideoRepository.Input(video=video, uuid=data.uuid)
        insert_data = self.__upload_video_repository.upload_video(upload_data)

        await self.__insert_video_repository.insert_video(insert_data)
