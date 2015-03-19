import importlib
import inspect
import os
from uuid import uuid4 as get_uuid


class Extension(object):
    def __init__(self, cls):
        if cls.__name__[0] == '_':
            raise InvalidFunctionName('Cannot init extension against a class starting with _')
        self._name = cls.__name__
        self._cls = cls
        # TODO: Determine if str or UUID object is preferable.
        self._id = str(get_uuid())
        self._register()

    def _register(self):
        ExtensionRegistry.modules[self._id] = self._cls


class ExtensionRegistry(object):
    modules = {}

    @staticmethod
    def get(id):
        return ExtensionRegistry.modules[id]

    @staticmethod
    def list():
        return ExtensionRegistry.modules


class ExtensionLoader(object):
    @staticmethod
    def load(path):
        # TODO: make chdir a context manager.
        os.chdir(path)
        # TODO: decide to read yaml or read dir structure?
        for ext_dir in [item for item in os.listdir('.') if os.path.isdir(item)]:
            module_name = '{0}.{1}.main'.format(os.path.split(path)[-1], ext_dir)
            print module_name
            loaded_module = importlib.import_module(module_name)
            # Extract instance of Extension from module
            for name, object in inspect.getmembers(loaded_module):
                if isinstance(object, Extension):
                    print object
                    print object._cls
                    print object._name
                    print '-' * 82


class InvalidFunctionName(Exception):
    pass