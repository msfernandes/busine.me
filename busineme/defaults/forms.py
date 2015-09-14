from abc import abstractmethod


class BusinemeForm(object):

    def __init__(self, request):
        self.data = request.POST
        self.user = request.user
        self.cleaned_data = {}
        self.errors = []
        self.extra = []

    @abstractmethod
    def is_valid(self):
        raise NotImplementedError()

    @abstractmethod
    def save(self):
        raise NotImplementedError()
