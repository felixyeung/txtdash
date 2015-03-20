from txtdash.content.provider import FunctionContentProvider
from txtdash.plugin.manager import PluginRegistry, PluginLoader
from txtdash.ui.box import Box

PluginLoader.load('plugins')

print PluginRegistry.list()
hello = PluginRegistry.get('RandomPlugin')
print hello

my_hello = hello(Box, FunctionContentProvider, 1, 10000000)
print my_hello.content.fetch()