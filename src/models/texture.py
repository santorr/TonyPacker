import cv2
import numpy as np
from PIL import Image


class Texture:
    """ This object represent a texture with RGB or RBGA channels """
    def __init__(self, _channel_r, _channel_g, _channel_b, _channel_a, _format, _resolution=(512, 512), _quality=95, _subsampling=0):
        self.resolution = _resolution
        self.format = _format
        self.quality = _quality
        self.subsampling = _subsampling
        self.channel_r = self.resize_channel(_channel_r)
        self.channel_g = self.resize_channel(_channel_g)
        self.channel_b = self.resize_channel(_channel_b)
        self.channel_a = self.resize_channel(_channel_a)

    def resize_channel(self, _data):
        """ Resize an array with a specific resolution """
        return cv2.resize(_data, dsize=self.resolution, interpolation=cv2.INTER_AREA)

    def compute_channels(self):
        """ Compute channels, if format has alpha merge as RGBA, else merge as RGB """
        if self.format['alpha']:
            return np.dstack((self.channel_r, self.channel_g, self.channel_b, self.channel_a))
        else:
            return np.dstack((self.channel_r, self.channel_g, self.channel_b))

    def save_texture(self, _full_path: str):
        """ Combine all channels before saving Image """
        _final_array = self.compute_channels()
        _image = Image.fromarray(_final_array.astype(np.uint8))
        _image.save(_full_path, quality=self.quality, subsampling=self.subsampling)
