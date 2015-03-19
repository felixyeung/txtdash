from txtdash.extension.manager import Extension

@Extension
class HelloWorld(object):
    def __init__(self):
        print 'A new Hello has been constructed!'