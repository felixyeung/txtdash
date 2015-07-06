import random
from txtdash.plugin.manager import Plugin
from txtdash.plugin.plugin_interface import PluginInterface

@Plugin
class RandomPlugin(PluginInterface):
    def __init__(self, box, function_content_provider, *args, **kwargs):
        # TODO, ensure self.box and self.content are present in an instance
        self.box = box()
        self.content = function_content_provider(random.randint, *args, **kwargs)

    def draw(self):
        self.box.window.addstr(1, 1, str(self.content.fetch()))
        self.box.draw()

    # TODO: remove this
    def say_something(self):
        print 'A new {0} has been constructed!'.format(self.__class__.__name__)
