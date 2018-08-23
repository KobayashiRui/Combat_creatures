import cv2
from base_camera import BaseCamera,BaseCamera2


class Camera(BaseCamera):
    video_source = 0
    def __init__(self,source):
        Camera.video_source = source
        print("Camera source {}".format(Camera.video_source))
        super().__init__()
        

    #@staticmethod
    #def set_video_source(source):
    #    Camera.video_source = source

    @staticmethod
    def frames():
        print(Camera.video_source)
        camera = cv2.VideoCapture(Camera.video_source)
        #camera.set(cv2.CAP_PROP_FPS,60)
        #camera.set(cv2.CAP_PROP_FRAME_WIDTH,320)
        #camera.set(cv2.CAP_PROP_FRAME_HEIGHT,240)
        print(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
        print(camera.get(cv2.CAP_PROP_FPS))
        if not camera.isOpened():
            raise RuntimeError('Could not start camera.')

        while True:
            # read current frame
            _, img = camera.read()

            # encode as a jpeg image and return it
            yield cv2.imencode('.jpg', img)[1].tobytes()

class Camera2(BaseCamera2):
    video_source = 0
    def __init__(self,source):
        Camera2.video_source = source
        print("Camera2 source {}".format(Camera2.video_source))
        super().__init__()
        

    #@staticmethod
    #def set_video_source(source):
    #    Camera.video_source = source

    @staticmethod
    def frames():
        print(Camera2.video_source)
        camera = cv2.VideoCapture(Camera2.video_source)
        #camera.set(cv2.CAP_PROP_FPS,60)
        #camera.set(cv2.CAP_PROP_FRAME_WIDTH,320)
        #camera.set(cv2.CAP_PROP_FRAME_HEIGHT,240)
        print(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
        print(camera.get(cv2.CAP_PROP_FPS))
        if not camera.isOpened():
            raise RuntimeError('Could not start camera.')

        while True:
            # read current frame
            _, img = camera.read()

            # encode as a jpeg image and return it
            yield cv2.imencode('.jpg', img)[1].tobytes()
