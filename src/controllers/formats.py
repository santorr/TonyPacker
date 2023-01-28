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
        return [_format['extension'] for _format in self._formats]

    def get_formats(self):
        return self._formats

    def get_export_formats(self):
        result = ''
        for i in range(len(self._formats)):
            if i < len(self._formats) - 1:
                result += f"{self._formats[i]['name']} (*{self._formats[i]['extension']});; "
            else:
                result += f"{self._formats[i]['name']} (*{self._formats[i]['extension']})"
        return result

    def get_format(self, _format_extension=None, _format_name=None):
        """ Return a format dict """
        if _format_extension is not None:
            for _format in self._formats:
                if _format_extension == _format['extension']:
                    return _format
        else:
            for _format in self._formats:
                if _format_name == _format['name']:
                    return _format
        return
