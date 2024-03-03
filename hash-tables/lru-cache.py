from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.od = OrderedDict()
        
    def get(self, key: int) -> int:
        if key not in self.od:
            return -1
        else:
            self.od.move_to_end(key)
            return self.od[key]

    def put(self, key: int, value: int) -> None:
        if key in self.od:
            self.od.move_to_end(key)

        self.od[key] = value
        
        if self.capacity < len(self.od):
            # Pairs in Fifo (First in First Out)
            self.od.popitem(False)
    
    def __str__(self):
        return str(self.od)
    
    def __repr__(self):
        return str(self.od)
        


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
obj.get(1)
obj.put(1,1)
obj.put(2,2)
obj.put(3,3)
obj.get(3)

print(obj)