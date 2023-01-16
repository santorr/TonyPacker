import cv2
import numpy as np
from PIL import Image


class ModelTexture:
    def __init__(self, _channel_r, _channel_g, _channel_b, _channel_a, _resolution=(512, 512)):
        print("Create texture data")
        self.resolution = _resolution

        self.channel_r = self.resize_channel(_channel_r)
        self.channel_g = self.resize_channel(_channel_g)
        self.channel_b = self.resize_channel(_channel_b)
        self.channel_a = self.resize_channel(_channel_a)
        print("Texture data created")

    def resize_channel(self, _data):
        """ Resize an array with a specific resolution """
        return cv2.resize(_data, dsize=self.resolution, interpolation=cv2.INTER_AREA)

    def final_array(self):
        """ Create a base array with a desired resolution """
        return np.dstack((self.channel_r, self.channel_g, self.channel_b, self.channel_a))

    def save_image(self, _full_path: str):
        _final_array = self.final_array()
        _image = Image.fromarray(_final_array.astype(np.uint8))
        _image.save(_full_path)
        print(f"Saved texture : {_full_path}")
