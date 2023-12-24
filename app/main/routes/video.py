from app.main.factories.video import make_db_upload_video, make_db_remove_video
from app.schemas.common import MessageResponse, VIDEO_UPLOAD_DESCRIPTION
from app.schemas.media import MediaInput, RemoveVideoInput
from app.main.dependencies import VideoFile
from app.schemas.common import PATH_UUID
from fastapi import Depends, UploadFile
from fastapi.routing import APIRouter
from app.infra.auth import JwtBearer
from app.main.config import PREFIX
from typing import Annotated


router = APIRouter(prefix=f"{PREFIX}/video", tags=['Video'])


@router.post(
    "/upload",
    status_code=200,
    summary="Upload a Video",
    response_description="Video Uploaded",
    response_model=MessageResponse,
    description=VIDEO_UPLOAD_DESCRIPTION
)
async def upload_video(
    uuid: Annotated[str, Depends(JwtBearer())],
    video: Annotated[UploadFile, Depends(VideoFile())]
):
    db_upload_video = make_db_upload_video()
    file = await video.read()

    data = MediaInput(uuid=uuid, file=file)
    await db_upload_video.upload_video(data)

    return MessageResponse(message="Video uploaded successfully")


@router.delete(
    "/remove/{video_uuid}",
    status_code=200,
    summary="Remove a Video",
    response_description="Video Removed",
    response_model=MessageResponse
)
async def remove_video(
    uuid: Annotated[str, Depends(JwtBearer())],
    video_uuid: PATH_UUID
):
    db_remove_video = make_db_remove_video()
    video_input = RemoveVideoInput.make(uuid, video_uuid)
    await db_remove_video.remove_video(video_input)

    return MessageResponse(message="Video removed successfully")
