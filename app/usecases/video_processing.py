from app.data.protocols.video import VideoProcessingRepository


class VideoProcessing(VideoProcessingRepository):

    def __init__(self) -> None:
        pass

    def handle(self, file: bytes) -> bytes:
        return file

        # FILE = "video.mp4"

        # with open(FILE, "wb") as file:
        #     file.write(data.file)

        # # cap = cv2.VideoCapture(FILE)
        # # fourcc = cv2.VideoWriter_fourcc(*'XVID')
        # # print(type(fourcc))
        # # # fourcc = cv2.VideoWriter.fourcc("DIB")
        # # video = cv2.VideoWriter(FILE, fourcc, 30.0, (1024, 512))

        # # while cap.isOpened():
        # #     _, frame = cap.read()
        # #     frame = cv2.flip(frame, 0)
        # #     video.write(frame)

        # # cap.release()
        # # video.release()

        # cap = cv2.VideoCapture(FILE)
        # width = int(cap.get(3))
        # height = int(cap.get(4))
        # fps = cap.get(5)
        # fourcc = cv2.VideoWriter_fourcc(*'XVID')
        # print(type(fourcc))
        # out = cv2.VideoWriter("enhanced_video.avi", fourcc, fps, (width * 2, height * 2))

        # while cap.isOpened():
        #     ret, frame = cap.read()
        #     if not ret:
        #         break

        #     resized_frame = cv2.resize(frame, (width * 2, height * 2))

        #     # Perform other enhancement operations if needed
        #     # For example, you can apply filters, denoising, or color correction here

        #     out.write(resized_frame)

        # cap.release()
        # out.release()
