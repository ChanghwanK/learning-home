class HashUtils:
    @classmethod
    def gen_key(cls, data):
        return hash(data)

    @classmethod
    def hash_func(cls, data):
        return data % 8


class BasicHashTable:
    def __init(self, size):
        self._store = [0 for _ in range(size)]

    def save(self, hash_value, value):
        self._store[hash_value] = value


hash_key = HashUtils.gen_key('Andy')
hash_address = HashUtils.hash_func(hash_key)

my_hash = BasicHashTable(8)
my_hash.save(hash_address, 'Andy')


class HashTable:
    def __init(self, size):
        self._store = [0 for _ in range(size)]

    def chaining_save(self, key, hash_value, value):
        if self._store[hash_value] != 0:
            for index in range(len(self._store[hash_value])):
                if self._store[hash_value][index][0] == key:
                    self._store[hash_value][index][1] = value
                    return
                self._store[hash_value].append([key, value])
        else:
            self._store[hash_value] = [[key, value]]

    def linear_save(self, key, hash_value, value):
        if self._store[hash_value] != 0:
            for index in range(hash_value, len(self._store)):
                if self._store[index] == 0:
                    self._store[index] = [key, value]
                    return
                elif self._store[index][0] == key:
                    self._store[index][1] = value
                    return
        else:
            self._store[hash_value] = [key, value]

    def chaining_get_data(self, index_key, hash_value):
        if self._store[hash_value] != 0:
            for index in range(len(self._store[hash_value])):
                if self._store[hash_value][index][0] == index_key:
                    return self._store[hash_value][index][1]
        else:
            return None

    def linear_get_data(self, index_key, hash_value):
        if self._store[hash_value] != 0:
            for index in range(hash_value, len(self._store)):
                if self._store[index] == 0:
                    return
                elif self._store[index][0] == index_key:
                    return self._store[index][1]
        else:
            return None
