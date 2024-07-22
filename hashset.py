class HashSet:
    DEF_SIZE = 100

    def __init__(self, size: int = None):
        if size is None:
            size = self.DEF_SIZE
        self.arr = size * [None]
        self.size = size

    def hash(self, value: int):
        return value % self.size

    def put(self, value: int) -> None:
        hashed = self.hash(value)
        for i in range(hashed, self.size*2):
            try_hash = i % self.size
            if self.arr[try_hash] is None:
                self.arr[try_hash] = value
                print(f"Value {value} got key {try_hash}")
                return None
        print("No free hashes")

    def get(self, value: int) -> bool:
        hashed = self.hash(value)
        for i in range(hashed, self.size*2):
            try_hash = i % self.size
            if self.arr[try_hash] == value:
                return True
        return False

set = HashSet()
set.put(10)
set.put(22)
set.put(101)
set.put(1)
print(set.get(10), set.get(20))

