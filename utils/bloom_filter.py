import math
import hashlib
from bitarray import bitarray
import pickle
import os


def read_bf():
    if os.path.exists('users.pkl'):
        bf = BloomFilter.load()
    else:
        print("Creating new bloomfilter...")
        bf = BloomFilter(size=1000000, hash_count=14)
    return bf

class BloomFilter:
    def __init__(self, size, hash_count):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)
        self.save()

    def add(self, item):
        digests = []
        for i in range(self.hash_count):
            digest = int(hashlib.sha256((str(item) + str(i)).encode('utf-8')).hexdigest(), 16) % self.size
            digests.append(digest)
            self.bit_array[digest] = 1

    def check(self, item):
        for i in range(self.hash_count):
            digest = int(hashlib.sha256((str(item) + str(i)).encode('utf-8')).hexdigest(), 16) % self.size
            if self.bit_array[digest] == 0:
                return False
        return True

    def save(self):
        with open('users.pkl', 'wb') as f:
            pickle.dump(self, f)
        print(f"bloomFilter saved to users.pkl")

    @classmethod
    def load(cls):
        with open("users.pkl", 'rb') as f:
            bloom_filter = pickle.load(f)
        print(f"BloomFilter loaded from users.pkl")
        return bloom_filter


if __name__ == "__main__":
    pass