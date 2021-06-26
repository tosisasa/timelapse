import cv2
import picamera
import picamera.array
from datetime import datetime

cascade_file = "/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml"

with picamera.PiCamera() as camera:
    camera.resolution = (640, 368)
    camera.rotation = 90
    with picamera.array.PiRGBArray(camera) as output:
        while True:
            output.seek(0)
            output.truncate(0)
            camera.capture(output, 'bgr')
            gray = cv2.cvtColor(output.array, cv2.COLOR_RGB2GRAY)
            cascade = cv2.CascadeClassifier(cascade_file)
            faces = cascade.detectMultiScale(gray, minSize=(120, 120))

            for (x, y, w, h) in faces:
                color = (0, 0, 255)
                cv2.rectangle(output.array, (x, y), (x+w, y+h), color, thickness = 2)

            if len(faces) != 0:
                now = datetime.now()
                filename = now.strftime("%Y%m%d_%H%M%S%f.jpg")
                cv2.imwrite(filename, output.array)

            cv2.imshow('frame', output.array)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
