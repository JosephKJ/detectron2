import random
from collections import deque


class Store:
    def __init__(self, total_num_classes, items_per_class, shuffle=True):
        self.shuffle = shuffle
        self.store = [deque(maxlen=items_per_class) for _ in range(total_num_classes)]

    def add(self, items, class_ids):
        for idx, class_id in enumerate(class_ids):
            self.store[class_id].append(items[idx])

    def retrieve(self):
        items = []
        for item in self.store:
            items.extend(list(item))
        if self.shuffle:
            random.shuffle(items)
        return items

    def __str__(self):
        s = self.__class__.__name__ + '('
        for idx, item in enumerate(self.store):
            s += '\n Class ' + str(idx) + ' --> ' + str(len(list(item))) + ' items'
        s = s + ' )'
        return s

    def __repr__(self):
        return self.__str__()

if __name__ == "__main__":
    store = Store(10, 3)
    store.add(('a', 'b', 'c', 'd', 'e', 'f'), (1, 1, 9, 1, 0, 1))
    store.add(('h',), (4,))
    print(store.retrieve())
    print(store)
