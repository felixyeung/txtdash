from txtdash.plugin.manager import PluginRegistry, PluginLoader

PluginLoader.load('/Users/fyeung/Documents/curses/plugins')

print PluginRegistry.list()

hello = PluginRegistry.get('HelloWorld')

print hello

my_hello = hello()