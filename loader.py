import pprint


class KnowledgeBaseService(object):
    def __init__(self, filepath):
        self.filepath = filepath
        self.rules = []
        self.domains = {}

    def load(self):
        with open(self.filepath, 'r', encoding='utf-8') as file:
            for line in file:
                if line.startswith('D'):
                    domain, meaning = line.strip().split(':')
                    if domain[2:].startswith('R'):
                        self.domains[domain[4:]] = {'mean': meaning.split(','),
                                                    'request': True}
                    else:
                        self.domains[domain[2:]] = {'mean': meaning.split(','),
                                                    'request': False}
                elif line.startswith('R'):
                    situation, production = line.strip().split('->')
                    self.rules.append({'situation': situation[2:],
                                       'production': production})

    def save(self, filepath=None):
        pass

    def add_rule(self, rule):
        if rule:
            self.rules.append(rule)
