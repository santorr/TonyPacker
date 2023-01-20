from os.path import abspath, join, normpath
import sys


def package_file_path(rel_path="", unix=True):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = abspath("")
    if unix:
        return normpath(join(base_path, rel_path)).replace("\\", "/")
    else:
        return normpath(join(base_path, rel_path))
