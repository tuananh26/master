import cv2
import pathlib

SOURCE_IMAGE = pathlib.Path(__file__).parent / 'src/image'


def convert_path(path):
    return '/'.join(str(path).split('\\'))


img_x = cv2.imread(convert_path(SOURCE_IMAGE/'x.PNG'))
img_o = cv2.imread(convert_path(SOURCE_IMAGE/'o.PNG'))
