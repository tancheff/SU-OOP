class dictionary_iter:
    def __init__(self, collection: dict):
        self.collection = list(collection.items())
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.collection) - 1:
            raise StopIteration

        self.index += 1

        return self.collection[self.index]


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

