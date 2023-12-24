from app.data.protocols.photo import ImageProcessingRepository
from numpy import frombuffer, uint8, array, zeros
from app.main.exceptions import InternalError
from PIL.Image import fromarray
from PIL.Image import Image
from cv2 import (
    addWeighted,
    imdecode,
    filter2D,
    cvtColor,
    resize,
    COLOR_BGR2RGB,
    IMREAD_COLOR,
    INTER_AREA,
)


class ImageProcessing(ImageProcessingRepository):
    SIZE = 600
    BRIGHTNESS = 1.2
    CONTRAST = 1.2
    KERNEL = [[0, -1, 0], [-1, 5, -1], [0, -1, 0]]

    def __init__(self) -> None:
        pass

    def handle(self, file: bytes) -> Image:
        try:
            bytes_array = frombuffer(file, uint8)
            image = imdecode(bytes_array, IMREAD_COLOR)
        except Exception:
            raise InternalError("Could not decode the image")

        height, width, _ = image.shape
        aspect_ratio = min(height, width) / max(height, width)

        if aspect_ratio <= 0.4:
            raise InternalError("Invalid image aspect ratio")

        if width < height:
            try:
                image = image[:width, :]
            except Exception:
                raise InternalError("Error in cropping the image")

        elif width > height:
            margin = int((width - height) / 2)
            try:
                image = image[:, margin:height + margin]
            except Exception:
                raise InternalError("Error in cropping the image")

        if width > self.SIZE:
            width, height = (self.SIZE, self.SIZE)
            try:
                image = resize(image, (width, height), interpolation=INTER_AREA)
            except Exception:
                raise InternalError("Error in resizing the image")

        try:
            kernel = array(self.KERNEL)
            image = filter2D(image, -1, kernel)
        except Exception:
            raise InternalError("Error in sharpening the image")

        try:
            source = zeros(image.shape, image.dtype)
            image = addWeighted(image, self.CONTRAST, source, 0, self.BRIGHTNESS)
        except Exception:
            raise InternalError("Error in enhancing the image")

        try:
            image = cvtColor(image, COLOR_BGR2RGB)
            image = fromarray(image)
        except Exception:
            raise InternalError("Error in converting the image")

        return image
