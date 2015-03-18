from uuid import uuid4 as get_uuid


class Extension(object):
    def __init__(self, cls):
        if cls.__name__[0] == '_':
            raise InvalidFunctionName('Cannot init extension against a class starting with _')
        self._name = cls.__name__
        self._func = cls
        self._id = get_uuid()

    def _register(self):
        ExtensionRegistry[self._id] = self.cls


class ExtensionRegistry(object):
    modules = {}

    def get(cls, id):
        return cls.modules[id]


class ExtensionLoader(object):
    """
    The extension loader should read from a path and load all modules in that path
    """
    pass


class InvalidFunctionName(Exception):
    pass