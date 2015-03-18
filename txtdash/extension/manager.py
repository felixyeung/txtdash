from uuid import uuid4 as get_uuid


class Extension(object):
    def __init__(self, cls):
        if cls.__name__[0] == '_':
            raise InvalidFunctionName('Cannot init extension against a class starting with _')
        self._name = cls.__name__
        self._cls = cls
        self._id = get_uuid()

    def _register(self):
        ExtensionRegistry[self._id] = self._cls


class ExtensionRegistry(object):
    modules = {}

    @staticmethod
    def get(id):
        return cls.modules[id]

    @staticmethod
    def list():
        print ExtensionRegistry.modules


class ExtensionLoader(object):
    """
    The extension loader should read from a path and load all modules in that path
    """
    @staticmethod
    def load(path):
        # TODO
        pass


class InvalidFunctionName(Exception):
    pass