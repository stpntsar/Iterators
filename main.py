class FlatIterator:

    def __init__(self, new_list):
        self.new_list = new_list

    def __iter__(self):
        self.list_iter = iter(self.new_list)
        self.nested_list = []
        self.cursor = -1
        return self

    def __next__(self):
        self.cursor += 1
        if len(self.nested_list) == self.cursor:
            self.nested_list = None
            self.cursor = 0
            while not self.nested_list:
                self.nested_list = next(self.list_iter)
        return self.nested_list[self.cursor]

def flat_generator(my_list):
    for sub_list in my_list:
        for item in sub_list:
            yield item

if __name__ == '__main__':
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]

    for item in FlatIterator(nested_list):
        print(item)

    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)

    for item in flat_generator(nested_list):
        print(item)