import os
from threading import Lock


class MetadataDict:

    def __init__(self):

        self.lock = Lock()
        self.metadata_dict = dict()

    def get(self, key):

        self.lock.acquire()
        metadata = self.metadata_dict[key]
        self.lock.release()

        return metadata

    def store(self, key, value):

        self.lock.acquire()
        self.metadata_dict[key] = value
        self.lock.release()


class Metadata:

    def __init__(self, filepath):

        with open(filepath, 'r') as fl:
            self.filename = os.path.split(filepath)[-1]
            self.column_names = fl.readline().split(',')
            self.num_rows = 0

            for _ in fl.readlines():
                self.num_rows += 1

    def to_dict(self):

        return {
            'filename': self.filename,
            'num_rows': self.num_rows,
            'column_names': self.column_names
        }
