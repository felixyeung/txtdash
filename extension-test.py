from txtdash.extension.manager import ExtensionRegistry, ExtensionLoader

ExtensionLoader.load('/Users/fyeung/Documents/curses/extensions')

for each in ExtensionRegistry.list():
    a_class = ExtensionRegistry.get(each)
    print a_class
    a_class()