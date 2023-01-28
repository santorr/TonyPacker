class Formats:
    _formats = [
        {
            "name": "JEPG",
            "extension": ".jpeg",
            "alpha": False
        },
        {
            "name": "JPG",
            "extension": ".jpg",
            "alpha": False
        },
        {
            "name": "PNG",
            "extension": ".png",
            "alpha": True
        },
        {
            "name": "TARGA",
            "extension": ".tga",
            "alpha": True
        }
    ]

    def get_extension_list(self):
        """ Get the list of formats extension"""
        return [_format['extension'] for _format in self._formats]

    def get_formats(self):
        """ Get all formats """
        return self._formats

    def get_export_formats(self):
        """ Get export format as string """
        return ''.join(f"{self._formats[i]['name']} (*{self._formats[i]['extension']});; " if i < len(self._formats) - 1 else f"{self._formats[i]['name']} (*{self._formats[i]['extension']})" for i in range(len(self._formats)))

    def get_format(self, _format_extension=None):
        """ Return a format dict from a format extension"""
        for _format in self._formats:
            if _format_extension == _format['extension']:
                return _format
        return
