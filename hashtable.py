# Creating a hash map class that will store the package objects
import package


class HashTable:
    def __init__(self):
        self.map = None
        self.table_size = 40
        self.table = [None] * self.table_size

    def set(self, key, value):

        hashed_key = self._hash_algo(key)
        hashed_value = [key, value]

        if self.table[hashed_key] is None:

            self.table[hashed_key] = list([hashed_value])
            return True
        else:

            for pair in self.table[hashed_key]:
                if pair[0] == key:
                    pair[1] = value
                    return True

            self.table[hashed_key].append(hashed_value)
            return True

    def get(self, key):
        hashed_key = self._hash_algo(key)

        if self.table[hashed_key] is not None:

            for pair in self.table[hashed_key]:
                if pair[0] == key:
                    return pair[1]

    def add(self, key, package):
        hashed_key = self._hash_algo(key)
        hashed_value = [key, package]

        if self.map[hashed_key] is None:
            self.map[hashed_key] = list([hashed_value])
            return True
        else:
            for pair in self.map[hashed_key]:
                if pair[0] == key:
                    pair[1] = package
                    return True

    def delete(self, key):
        hashed_key = self._hash_algo(key)

        if self.table[hashed_key] is None:
            return False

        for i in range(0, len(self.table[hashed_key])):
            if self.table[hashed_key][i][0] == key:
                self.table[hashed_key].pop(i)
                return True

    def print_hash_table(self):
        print("_________HASH TABLE_________")
        for entry in self.table:
            if entry is not None:
                print(str(entry))

    def _hash_algo(self, key):

        return key % self.table_size
