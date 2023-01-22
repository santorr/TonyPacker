class Formats:
    def __init__(self):
        self._formats = \
            [
                {
                    'name': 'JPG',
                    'extension': '.jpg',
                    'alpha': False
                },
                {
                    'name': 'JPEG',
                    'extension': '.jpeg',
                    'alpha': False
                },
                {
                    'name': 'PNG',
                    'extension': '.png',
                    'alpha': True
                },
                {
                    'name': 'TGA',
                    'extension': '.tga',
                    'alpha': True
                }
            ]

    def get_export_formats(self):
        """ Return a string from all formats ('JPG (*jpg);; PNG (*png) ...') """
        _result = ''
        for i in range(len(self._formats)):
            _result += f"{self._formats[i]['name']} (*{self._formats[i]['extension']})"
            if i < len(self._formats) - 1:
                _result += " ;;"
        return _result

    def get_format_data_from_extension(self, _extension):
        """ Return data (name, extension, alpha) from an extension (.jpg) """
        return next((_format for _format in self._formats if _format['extension'] == _extension), None)
