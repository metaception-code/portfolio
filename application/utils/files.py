import json
import os

from application.local_settings import ROOT_FILEPATH

def get_static_file(path):
    return os.path.join(ROOT_FILEPATH, path)


def get_static_json(path):
    return json.load(open(get_static_file(path)))
