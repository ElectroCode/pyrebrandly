from beautifultable import BeautifulTable


class Format:
    def __init__(self, cls, command, json):
        self.cls = cls
        self.command = command
        self.json = json

    def format(self):
        """Format json according to class(Links, Domains, Account) and command(list, add, etc.)
        """

        if self.cls == 'domains':
            if self.command == 'list':
                return self.make_table(self.cls, self.command)

    def make_table(self, cls, command):
        """Return Table instance as raw string
        """

        json = self.json
        tables = []
        if cls == 'links':
            pass
        if cls == 'domains':
            if command == 'list':
                for domain in json:
                    table = self.build_table(domain)
                    tables.append(table)

                return tables
    @staticmethod
    def build_table(json):
        table = BeautifulTable(json)
        return table