from txtdash.content.provider import FunctionContentProvider
from txtdash.plugin.manager import PluginRegistry, PluginLoader


class FakeBox(object):
    pass


PluginLoader.load('plugins')

print PluginRegistry.list()
hello = PluginRegistry.get('RandomPlugin')
print hello

my_hello = hello(FakeBox, FunctionContentProvider, 1, 10000000)
print my_hello.content.fetch()
my_hello.say_something()
