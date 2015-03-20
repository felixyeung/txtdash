from txtdash.plugin.manager import Plugin

@Plugin
class HelloWorld(object):
    def __init__(self):
        print 'A new Hello has been constructed!'