from .video import router as video_router
from .photo import router as photo_router


ROUTES = (
    video_router,
    photo_router
)
