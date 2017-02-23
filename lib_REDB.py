# coding=utf-8
class REDB(object):
    """docstring for REDB."""

    data = {
        'rlt': {},
        'exp': {}
    }

    def __init__(self, debug=False):
        super(REDB, self).__init__()
        self.debug = debug

    def save(self, path, data):
        pass

    def load(self, path):
        return data

    def add_relation(self, value):
        return key

    def add_explanation(self, key, value, type):
        pass

    def find_relation(self, value):
        return key

    def find_explanation(self, value):
        return key
