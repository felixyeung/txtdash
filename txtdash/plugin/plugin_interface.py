class PluginInterface(object):
    def __init__(self):
        raise NotImplementedError('Incomplete Plugin \'{0}\''.format(self.__class__.__name__))

    def draw(self):
        raise NotImplementedError('Incomplete Plugin \'{0}\''.format(self.__class__.__name__))
