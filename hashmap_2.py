class HashMap:
    def insert(self, key, value):
        # ?

        index = self.key_to_index(key)
        self.hashmap[index] = (key, value)

    def resize(self):
        if len(self.hashmap) == 0:
            self.hashmap.append() = [None]
            load = self.get_load()
            if load >= 5:
                new_size = len(self.hashmap) * 10
                self.hashmap = [None for i in range(new_size)]


    def current_load(self):
        count = 0
        for i in self.hashmap:
            if i != None:
                count += 1
        return (count / len(self.hashmap)) * 100

    # don't touch below this line

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def key_to_index(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % len(self.hashmap)

    def __repr__(self):
        final = ""
        for i, v in enumerate(self.hashmap):
            if v != None:
                final += f" - {str(v)}\n"
        return final

class HashMap:
    def insert(self, key, value):
        self.resize()
        index = self.key_to_index(key)
        self.hashmap[index] = (key, value)

    def resize(self):
        if len(self.hashmap) == 0:
            self.hashmap = [None]
            return
        load = self.current_load()
        if load < 0.05:
            return
        old_hashmap = self.hashmap.copy()
        self.hashmap = [None] * (len(old_hashmap) * 10)
        for kvp in old_hashmap:
            if kvp is not None:
                self.insert(kvp[0], kvp[1])

    def current_load(self):
        if len(self.hashmap) == 0:
            return 1
        filled_slots = 0
        for slot in self.hashmap:
            if slot is not None:
                filled_slots += 1
        return filled_slots / len(self.hashmap)

    # don't touch below this line

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def key_to_index(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % len(self.hashmap)

    def __repr__(self):
        final = ""
        for i, v in enumerate(self.hashmap):
            if v != None:
                final += f" - {str(v)}\n"
        return final

