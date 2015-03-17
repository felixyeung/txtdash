from abc import abstractmethod


class ContentProvider(object):
    @abstractmethod
    def fetch(self):
        pass


class FunctionContentProvider(ContentProvider):
    pass


class StaticContentProvider(ContentProvider):
    def __init__(self, value):
        self.value = value

    def fetch(self):
        return self.value


class FileContentProvider(ContentProvider):
    def __init__(self, file_path):
        self.file_path = file_path

    def fetch(self):
        with open(self.file_path, 'r') as f:
            return f.read()

    def fetch_lines(self):
        with open(self.file_path, 'r') as f:
            for line in f:
                yield line


class DynamicContentProvider(ContentProvider):
    def __init__(self, request):
        # TODO: instead of accepting an URI string, maybe get a request object?
        self.request = request

    def fetch(self):
        # return self.request.get()
        pass