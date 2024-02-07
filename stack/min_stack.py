class MinStack:

    def __init__(self):
        lists = []
        self.lists = lists
        
    def push(self, val: int) -> None:
        self.lists.append(val)
        return None

    def pop(self) -> None:
        self.lists.pop()
        return None

    def top(self) -> int:
        return self.lists[-1]
        

    def getMin(self) -> int:
        return min(self.lists)