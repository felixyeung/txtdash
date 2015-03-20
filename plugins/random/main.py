import random
from txtdash.plugin.manager import Plugin


@Plugin
class RandomPlugin(object):
    def __init__(self, box, content, *args, **kwargs):
        print 'A new {0} has been constructed!'.format(self.__class__.__name__)
        #self.box = box()
        self.content = content(random.randint, *args, **kwargs)