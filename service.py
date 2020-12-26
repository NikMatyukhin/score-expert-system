import pprint


class KnowledgeBaseService(object):
    def __init__(self, filepath):
        self.filepath = filepath
        self.rules = []
        self.facts = {}

    def load(self):
        with open(self.filepath, 'r', encoding='utf-8') as file:
            for line in file:
                if line.startswith('D'):
                    fact, meaning = line.strip().split(':')
                    if fact[2:].startswith('R'):
                        self.facts[fact[4:]] = {'mean': meaning.split(','),
                                                'request': True}
                    else:
                        self.facts[fact[2:]] = {'mean': meaning.split(','),
                                                'request': False}
                elif line.startswith('R'):
                    situation, production = line.strip().split('->')
                    self.rules.append({'situation': situation[2:].strip(),
                                       'production': production.strip()})

    def save(self, filepath=None):
        pass

    def add_rule(self, rule: dict):
        if rule:
            self.rules.append(rule)

    def delete_rule(self, rule: dict):
        if rule:
            try:
                self.rules.remove(rule)
            except ValueError:
                return

    def add_fact(self, fact: dict):
        if fact:
            self.facts.update(fact)

    def delete_fact(self, fact: str):
        if fact in self.facts:
            del self.facts[fact]

    def update_meaning(self, fact: str, meanings: list):
        if fact in self.facts and meanings:
            self.facts[fact]['mean'] = meanings
