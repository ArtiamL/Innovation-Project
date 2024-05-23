import argparse
import sys
import time
import os

from PyQt5.QtCore import QThread, Qt, pyqtSignal, QLibraryInfo
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QLabel, QMainWindow

from gpiozero import Button

import cv2
from tflite_support.task import core, processor, vision

# os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = QLibraryInfo.location(
    # QLibraryInfo.PluginsPath
# )

class Thread(QThread):
    changePixmap = pyqtSignal(QImage)
    collected = pyqtSignal(str, name='collected')

    def run(self, model: str, max_results: int, score_threshold: float, num_threads: int,
        enable_edgetpu: bool, camera_id: int, width: int, height: int):

        self.isRunning = True

        allow_list = []

        with open("../image_classification/labels.txt", "r") as f:
            allow_list = f.read().splitlines()

        # print(allow_list)

        base_options = core.BaseOptions(file_name=model, use_coral=enable_edgetpu, num_threads=num_threads)

        classification_options = processor.ClassificationOptions(
        max_results=max_results, score_threshold=score_threshold, 
        category_name_allowlist=allow_list)
        options = vision.ImageClassifierOptions(base_options=base_options, classification_options=classification_options)

        classifier = vision.ImageClassifier.create_from_options(options)

        btn = Button(26)

        cap = cv2.VideoCapture(camera_id)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

        while cap.isOpened():
            success, img = cap.read()
            if not success:
                sys.exit("ERROR: Cannot read from camera!")

            img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
            
            rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            
            h, w, ch = rgb_img.shape

            bytes_per_line = ch*w

            convert_to_Qt = QImage(rgb_img.data, w, h, bytes_per_line, QImage.Format_RGB888)

            # label.setPixmap(QPixmap.fromImage(convert_to_Qt))

            pic = convert_to_Qt.scaled(640, 480, Qt.KeepAspectRatio)


            self.changePixmap.emit(pic)
            
            if btn.is_pressed:

                tensor_img = vision.TensorImage.create_from_array(rgb_img)

                categories = classifier.classify(tensor_img)

                name = None

                Thread.sleep(1)
                
                if categories is not None:

                    for cat in categories.classifications[0].categories:
                        name = cat.category_name
                        print(f"Category: {cat.category_name}, Score: {str(round(cat.score, 2))}")

                
                if name is not None:
                    name = name.replace(' ', '_').lower()
                    cv2.imwrite(f"../collection/images/collected/{name}.png", rgb_img)

                    self.collected.emit(name)

                    cap.release()
                    break
                    

            if cv2.waitKey(1) == 27:
                break

    def stop(self):
        self.isRunning = False
        self.quit()
        self.terminate()

    def __name__(self):
        return "Thread"

def main():
  parser = argparse.ArgumentParser(
      formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument(
      '--model',
      help='Name of image classification model.',
      required=False,
      default='mobilenet_v2.tflite')
  parser.add_argument(
      '--maxResults',
      help='Max of classification results.',
      required=False,
      default=3)
  parser.add_argument(
      '--scoreThreshold',
      help='The score threshold of classification results.',
      required=False,
      type=float,
      default=0.0)
  parser.add_argument(
      '--numThreads',
      help='Number of CPU threads to run the model.',
      required=False,
      default=4)
  parser.add_argument(
      '--enableEdgeTPU',
      help='Whether to run the model on EdgeTPU.',
      action='store_true',
      required=False,
      default=False)
  parser.add_argument(
      '--cameraId', help='Id of camera.', required=False, default=0)
  parser.add_argument(
      '--frameWidth',
      help='Width of frame to capture from camera.',
      required=False,
      default=640)
  parser.add_argument(
      '--frameHeight',
      help='Height of frame to capture from camera.',
      required=False,
      default=480)
  args = parser.parse_args()

  th = Thread()

  Thread.run(None, args.model, int(args.maxResults),
      args.scoreThreshold, int(args.numThreads), bool(args.enableEdgeTPU),
      int(args.cameraId), args.frameWidth, args.frameHeight)

if __name__ == "__main__":
    main()