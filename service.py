import pprint


class KnowledgeBaseService(object):
    def __init__(self):
        self.rules = []
        self.facts = {}
        self.filepath = None
        self.unsaved = False

    def load(self, filepath):
        self.filepath = filepath
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
        if filepath:
            self.filepath = filepath

        with open(self.filepath, 'w', encoding='utf-8') as file:
            for fact, data in self.facts.items():
                line = 'D '
                if data['request']:
                    line += 'R '
                line = line + fact + ':' + ','.join(data['mean']) + '\n'
                file.write(line)
            for rule in self.rules:
                situation, production = rule['situation'], rule['production']
                line = 'R ' + situation + ' -> ' + production + '\n'
                file.write(line)
            self.unsaved = False

    def add_rule(self, rule: dict):
        if rule:
            self.rules.append(rule)
            self.unsaved = True

    def delete_rule(self, rule: dict):
        if rule:
            try:
                self.rules.remove(rule)
            except ValueError:
                return
            self.unsaved = True

    def add_fact(self, fact: dict):
        if fact:
            self.facts.update(fact)
            self.unsaved = True

    def delete_fact(self, fact: str):
        if fact in self.facts:
            del self.facts[fact]
            self.unsaved = True

    def update_meaning(self, fact: str, meanings: list):
        if fact in self.facts and meanings:
            self.facts[fact]['mean'] = meanings
            self.unsaved = True
