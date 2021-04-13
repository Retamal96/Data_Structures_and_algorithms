
class DumbQueue:

    def __init__(self):
        self.data = []
    
    def __len__(self):
        return len(self.data)

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        if len(self.data) == 0:
            raise ValueError('Queue is empty')
        return self.data.pop(0)
    

#Is faster but it doesnt resize use too much memory 
class FasterDumbQueue:

    def __init__(self):
        self._data = []
        self._front_index = 0

    def __len__(self):
        return len(self._data) - self._front_index

    # O(1)
    def enqueue(self, item):
        self._data.append(item)

    # O(1)
    def dequeue(self):
        if len(self._data) == 0 or self._front_index == len(self._data):
            raise ValueError("Queue is empty")
        item = self._data[self._front_index]
        self._data[self._front_index] = None
        self._front_index += 1
        return item

    # O(1)
    def front(self):
        if len(self._data) == 0 or self._front_index == len(self._data):
            raise ValueError("Queue is empty")
        return self._data[self._front_index]

class Stack:

    def __init__(self):
            self.data = []

    def __len__(self):
        return len(self.data)

    def push(self, item):
        self.data.append(item)

    def peek(self):
        if len(self.data) == 0:
            raise ValueError('Stack is empty')
        return self.data[len(self.data) - 1] 

    def pop(self):
        if len(self.data) == 0:
            raise ValueError('Stack is empty')
        return self.data.pop(len(self.data) - 1)

my_queue = FasterDumbQueue()

for number in range(10):
    my_queue.enqueue(number)

while len(my_queue) > 1:
    print(my_queue.dequeue())



"""
my_stack = Stack()

for number in range(13):
    my_stack.push(number)

while len(my_stack) > 0:
    print(my_stack.pop())"""