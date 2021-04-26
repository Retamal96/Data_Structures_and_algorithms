
class linked_list:

    def __init__(self):
        self._head = None
        self._tail = None
        self._number_of_items = 0

    def __len__(self):
        return self._number_of_items

    def front(self):
        if self._number_of_items == 0:
            raise ValueError('It's empty')
        
        return self._head

    def add_to_front(self, data):
        new_node = self.Node(data, self._head)
        self._head = new_node
        self._number_of_items +=1
        if self._head.next is None:
            self._tail = new_node

    def add_to_back(self, data):
        new_node = self.Node(data, None)
        if self._tail is None:
            self._tail = new_node
            self._head = new_node
        else:
            self._tail.next = new_node
        self._number_of_items +=1

    def remove_from_front(self):
        if self._number_of_items == 0:
            raise ValueError('It's empty')

        data = self._head.data

        self._head.data = None
        self._head = self._head.next

        if self._head is None:
            self._tail = None

        self._number_of_items -=1

    class Node:

        def __init__(self,data, next = None):
            self.data = data
            self.next = next 


class LLStack:

    def __init__(self):
        self._data = linked_list()

    def __len__(self):
        return len(self._data)

    def push(self, item):
        return self._data.add_to_front(item)

    def peek(self):
        return self._data.front()

    def pop(self):
        return self._data.remove_from_front()
    

class LLQueue:
     def __init__(self):
        self._data = linked_list()

    def __len__(self):
        return len(self._data)

    def front(self):
        return self._data.front()

    def enqueue(self, data):
        self._data.add_to_back(data)
    
    def dequeue(self):
        self._data.remove_from_front()


