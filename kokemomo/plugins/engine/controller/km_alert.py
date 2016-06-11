__author__ = 'hiroki-m'


class KMAlert(object):

    def __init__(self):
        self.list = []

    def add_data(self, type='info', id=None, message='', option=None):
        data = {}
        data['type'] = type
        data['id'] = id
        data['message'] = message
        data['option'] = option
        self.list.append(data)

    def have(self, id=None):
        for data in self.list:
            if data['id'] == id:
                return True
        return False

    def get(self, id=None):
        for data in self.list:
            if data['id'] == id:
                return data
        return None

    def size(self):
        return len(self.list)