from .photo import router as photo_router
from .video import router as video_router


ROUTES = (
    photo_router,
    video_router
)
