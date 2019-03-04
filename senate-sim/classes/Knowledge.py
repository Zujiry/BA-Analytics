import logging


class Knowledge:
    def __init__(self, family, education, integration, work, law, dataprotection, environment, economy, science, media, culture):
        self.knowledge = {
            "family": family,
            "education": education,
            "integration": integration,
            "work": work,
            "law": law,
            "dataprotection": dataprotection,
            "environment": environment,
            "economy": economy,
            "science": science,
            "media": media,
            "culture": culture
        }

    def influence(self, key, value, bond):
        self.knowledge[key] += ((value + bond)/10)
        if self.knowledge[key] > 100:
            self.knowledge[key] = 100

    def __str__(self):
        return str(self.knowledge)
