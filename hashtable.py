import package


class HashTable:
    """
    Custom hash table that creates an object and holds that data in a key/value pair.

    Algorithmic Complexity: O(1). Since the number of objects is known ahead of time and the fact that there
    will be no need for resizing and no keys being associated with multiple elements, it's only O(1) complexity.
    """
    def __init__(self):
        self.map = None
        # Initializes the number of buckets in the table
        self.table_size = 40
        # Initializes the hash table with the proper number of buckets
        self.table = [None] * self.table_size

    def set(self, key, value):
        """
        This function sets a key and value to an entry in the hash table that is dependent on the hashed value
        of the key. It also adds chaining functionality to the hash table. It does so by checking each sub-list
        in the buck, and resets its value to the given value if it already exists, and adds a new sub-list in
        the bucket if that key does not already exist. The chaining functionality allows the hash table to
        qualify as 'self-adjusting' to fulfill that requirement of this project

        Algorithmic Complexity: O(1). Since there are no instances of multiple objects being associated to one
        key, the complexity is O(1).
        """
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
        # This function returns a value of an entry that matches the given key in the hash table
        # Algorithmic Complexity: 0(1).

        # Creates a hashed key from the input for the key
        hashed_key = self._hash_algo(key)

        # If the bucket that maches the hashed key isn't empty
        if self.table[hashed_key] is not None:
            # Goes through every pair in the hash table
            for pair in self.table[hashed_key]:
                # If the first index of the pair equals the key
                if pair[0] == key:
                    # Returns the value
                    return pair[1]

    def delete(self, key):
        # This function removes an entry that matches the given key in the hash table
        # Algorithmic Complexity: O(1).

        # Creates a hashed key from the input for they key
        hashed_key = self._hash_algo(key)

        # Returns False if the pair for the given key is empty
        if self.table[hashed_key] is None:
            return False

        # For every element in the entire hash table, searches for a match of the given key
        for i in range(0, len(self.table[hashed_key])):
            if self.table[hashed_key][i][0] == key:
                # Deletes the entry that matches the key
                self.table[hashed_key].pop(i)
                return True

    def print_hash_table(self):
        # This function prints out each entry of the hash table to the CLI
        # Algorithmic Complexity: O(n)

        print("_________HASH TABLE_________")
        for entry in self.table:
            if entry is not None:
                print(str(entry))

    def _hash_algo(self, key):
        """
        This algorithm takes a number, hashes that number, and returns the value. Calculates the key given modulo
        of the size of the table. This creates a 1 to 1 mapping since it is already known that there will only be
        40 unique keys, so only 40 buckets will need to be created.

        Algorithmic Copmlexity: O(1).
        """
        return key % self.table_size
