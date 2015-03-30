import importlib
import inspect
import os
from uuid import uuid4 as get_uuid

from txtdash.plugin.exception import InvalidPluginError, RedefinePluginError


class Plugin(object):
    def __init__(self, cls):
        if cls.__name__[0] == '_':
            raise InvalidPluginError('Cannot init plugin against a class starting with _')
        self._name = cls.__name__
        self._cls = cls
        # TODO: Determine if str or UUID object is preferable.
        self._id = str(get_uuid())
        self._register()

    def _register(self):
        class_name = self._cls.__name__
        if class_name in PluginRegistry.modules:
            raise RedefinePluginError('Plugin {0} already defined'.format(class_name))
        PluginRegistry.modules[class_name] = self._cls


class PluginRegistry(object):
    modules = {}

    @staticmethod
    def get(id):
        return PluginRegistry.modules[id]

    @staticmethod
    def list():
        return PluginRegistry.modules


class PluginLoader(object):
    @staticmethod
    def load(path):
        # TODO: make chdir a context manager.
        os.chdir(path)
        # TODO: decide to read yaml or read dir structure?
        for plugin_dir in [item for item in os.listdir('.') if os.path.isdir(item)]:
            root_package = os.path.split(path)[-1]
            plugin_package = plugin_dir
            module_name = get_module_name(root_package, plugin_package, 'main')
            loaded_module = importlib.import_module(module_name)
            # Extract instance of Plugin (created with decorator) from module
            for name, object in inspect.getmembers(loaded_module):
                if isinstance(object, Plugin):
                    pass


def get_module_name(*args):
    return '.'.join(map(str, args))