import random
from txtdash.plugin.manager import Plugin


@Plugin
class RandomPlugin(object):
    def __init__(self, box, function_content_provider, *args, **kwargs):
        # TODO, ensure self.box and self.content are present in an instance
        self.box = box()
        self.content = function_content_provider(random.randint, *args, **kwargs)

    # TODO: remove this
    def say_something(self):
        print 'A new {0} has been constructed!'.format(self.__class__.__name__)
