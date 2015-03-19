import importlib
import inspect
import os
from uuid import uuid4 as get_uuid
import sys


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
        return ExtensionRegistry.modules[id]

    @staticmethod
    def list():
        print ExtensionRegistry.modules


class ExtensionLoader(object):
    """
    The extension loader should read from a path and load all modules in that path
    """

    @staticmethod
    def load(path):
        # TODO: make chdir a context manager.
        os.chdir(path)
        print 'hi'
        # TODO: decide to read yaml or read dir structure?
        for each in os.walk('.'):
            print each
        for ext_dir in [item for item in os.listdir('.') if os.path.isdir(item)]:
            ext_module = '{0}.{1}.main'.format(os.path.split(path)[-1], ext_dir)
            print ext_module
            my_mod = importlib.import_module(ext_module)
            for each in inspect.getmembers(my_mod):
                print each
                print '-' * 80

class InvalidFunctionName(Exception):
    pass