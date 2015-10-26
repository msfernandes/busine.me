class Terminal(object):

    def __init__(self):
        self.id = None
        self.description = ''
        self.address = ''


class Company(object):

    def __init__(self):
        self.id = None
        self.name = ''


class Busline(object):

    def __init__(self):
        self.id = None
        self.via = ''
        self.terminals = []
        self.fee = 0.0
        self.description = ''
        self.company = None
        self.route_size = 0.0
        self.line_number = ''
