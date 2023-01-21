import numpy as np
from PIL import Image


class ModelChannel:
    def __init__(self):
        """ Create default array of size 4 """
        self.default_size = (2, 2)
        self.data = np.ones(self.default_size, np.uint8)

    @staticmethod
    def clamp(_value, _minimum_value, _maximum_value):
        """ Clamp a value between a minimum and a maximum value """
        return max(min(_value, _maximum_value), _minimum_value)

    def fill_data_with_uniform_value(self, _value: int):
        """ Fill data with value, to make a uniform array (0, 255) """
        self.data = np.ones(self.default_size, np.uint8) * self.clamp(_value, 0, 255)

    def fill_data_with_image(self, _image_path: str):
        """ Fill data with an image, to make a uniform array (0, 255) """
        _image = Image.open(_image_path).convert('L')
        self.data = np.asarray(_image)

    def get_data(self):
        """ Return data at desired resolution """
        return self.data

    def get_data_size(self):
        """ Return a tuple for the data size (x, y) """
        return self.data.shape

    def get_image(self):
        """ Return an image based on data with original data size """
        return Image.fromarray(self.data)
