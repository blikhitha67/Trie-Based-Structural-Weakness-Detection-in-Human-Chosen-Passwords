# hashing/bloom_filter.py
import hashlib

class BloomFilter:
    def __init__(self, size=1000):
        self.size = size
        self.bit_array = [0] * size

    def _hashes(self, item):
        h1 = int(hashlib.md5(item.encode()).hexdigest(), 16) % self.size
        h2 = int(hashlib.sha1(item.encode()).hexdigest(), 16) % self.size
        return [h1, h2]

    def add(self, item):
        for h in self._hashes(item):
            self.bit_array[h] = 1

    def check(self, item):
        return all(self.bit_array[h] for h in self._hashes(item))

# Example usage
if __name__ == "__main__":
    bf = BloomFilter(size=500)
    leaked = ["123456", "password", "qwerty"]
    for pwd in leaked:
        bf.add(pwd)
    print(bf.check("123456"))  # True
    print(bf.check("admin"))   # False
