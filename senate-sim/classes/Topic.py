import logging


class Topic:
    persons = []

    # related - related knowledge
    def __init__(self, id, name, related, options):
        self.id = id
        self.name = name
        self.related = related
        self.options = options

    def get_related(self):
        return self.related
