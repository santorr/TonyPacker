import cv2
import numpy as np
from PIL import Image


class ModelChannel:
    def __init__(self):
        """ Create default array of size 4 """
        self.data = np.ones((4, 4), np.uint8)

    @staticmethod
    def clamp(_value, _minimum_value, _maximum_value):
        """ Clamp a value between a minimum and a maximum value """
        return max(min(_value, _maximum_value), _minimum_value)

    def fill_data_with_uniform_value(self, _value: int):
        """ Fill data with value, to make a uniform array (0, 255) """
        self.data = np.ones((4, 4), np.uint8) * self.clamp(_value, 0, 255)

    def fill_data_with_image(self, _image_path: str):
        """ Fill data with an image, to make a uniform array (0, 255) """
        _image = Image.open(_image_path).convert('L')
        self.data = np.asarray(_image)

    def get_data(self, _resolution=(1024, 1024)):
        """ Return data at desired resolution """
        return self.resize_array(_resolution)

    def get_image(self, _resolution=(1024, 1024)):
        return Image.fromarray(self.get_data(_resolution=_resolution))

    def resize_array(self, _resolution):
        """ Resize an array with a specific resolution """
        return cv2.resize(self.data, dsize=_resolution, interpolation=cv2.INTER_AREA)

    def save_image(self):
        Image.fromarray(self.data).save('test.jpg')
