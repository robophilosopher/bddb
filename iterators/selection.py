from iterators.iterator import Iterator

class Selection(Iterator):
    def __init__(self, node, predicatef):
        self.inputs = node
        self.predicatef = predicatef

    def __next__(self):
        while True:
            row = next(self.inputs)
            if self.predicatef(row):
                return row

    # Test helper method to make warning go away.
    # Might be otherwise useless.
    def close_file(self):
        self.inputs.close_file()
