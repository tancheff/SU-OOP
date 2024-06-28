class reverse_iter:
    def __init__(self, collection):
        self.collection = collection
        self.start_index = 0
        self.end_index = -(len(self.collection))

    def __iter__(self):
        return self

    def __next__(self):
        self.start_index -= 1
        if self.start_index < self.end_index:
            raise StopIteration()
        else:
            return self.collection[self.start_index]


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
