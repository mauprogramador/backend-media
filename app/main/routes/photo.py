from app.main.factories.photo import make_db_upload_photo, make_db_remove_photo
from app.schemas.common import MessageResponse, IMAGE_UPLOAD_DESCRIPTION
from app.main.dependencies import ImageFile
from app.main.dependencies import JwtBearer
from app.schemas.media import MediaInput
from fastapi import Depends, UploadFile
from fastapi.routing import APIRouter
from app.main.config import PREFIX
from typing import Annotated


router = APIRouter(prefix=f"{PREFIX}/photo", tags=['Photo'])


@router.post(
    "/upload",
    status_code=200,
    summary="Upload a Photo",
    response_description="Photo Uploaded",
    response_model=MessageResponse,
    description=IMAGE_UPLOAD_DESCRIPTION
)
async def upload_photo(
    uuid: Annotated[str, Depends(JwtBearer())],
    photo: Annotated[UploadFile, Depends(ImageFile())],
):
    db_upload_photo = make_db_upload_photo()
    file = await photo.read()

    data = MediaInput(uuid=uuid, file=file)
    await db_upload_photo.upload_photo(data)

    return MessageResponse(message="Photo uploaded successfully")


@router.delete(
    "/remove",
    status_code=200,
    summary="Remove a Photo",
    response_description="Photo Removed",
    response_model=MessageResponse
)
async def remove_photo(
    uuid: Annotated[str, Depends(JwtBearer())]
):
    db_remove_photo = make_db_remove_photo()
    await db_remove_photo.remove_photo(uuid)

    return MessageResponse(message="Photo removed successfully")
