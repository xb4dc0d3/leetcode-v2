from random import sample
class RandomizedSet:

    def __init__(self): 
        self.hash_table = set()
        

    def insert(self, val: int) -> bool:
        if val not in self.hash_table:
            self.hash_table.add(val)
            return True
        return False
        

    def remove(self, val: int) -> bool:
        if val in self.hash_table:
            self.hash_table.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        return sample(self.hash_table, k=1)[0]

    # def __repr__(self) -> str:
    #     return str(self.hash_table)     


obj = RandomizedSet()
param_1 = obj.insert(3)
param_2 = obj.remove(2)
param_3 = obj.getRandom()

print(obj)