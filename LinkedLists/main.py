
class DoublyLinkedList:

    class Position:

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def data(self):
            return self._node.data

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            return not ( self == other )

    def __init__(self):
        self._head = self.Node(None)   # Sentinel head/tail
        self._head.next = self._head # always the first node or itself if it's empty
        self._head.previous = self._head # always the last node or itself if it's empty
        self._number_of_items = 0

    def __len__(self):
        return self._number_of_items

    # O(1)
    def first(self):
        return self._make_position(self._head.next)

    # O(1)
    def last(self):
        return self._make_position(self._head.previous)

    # O(1)
    def after(self, position):
        node = self._validate(position)
        return self._make_position(node.next)

    # O(1)
    def before(self, position):
        node = self._validate(position)
        return self._make_position(node.previous)

    # O(1)
    def add_after(self, position, data):
        node = self._validate(position)
        return self._make_position(self._insert_between(data, previous=node, next=node.next))

    # O(1)
    def add_before(self, position, data):
        node = self._validate(position)
        return self._make_position(self._insert_between(data, previous=node.previous, next=node))

    # O(1)
    def delete(self, position):
        node = self._validate(position)
        return self._remove_node(node)

    # O(1)
    def replace(self, position, data):
        node = self._validate(position)
        original = node.data
        node.data = data
        return original

    def is_empty(self):
        return self._number_of_items == 0

    # O(1)
    def add_to_front(self, item):
        self._insert_between(item, next=self._head.next, previous=self._head)

    # O(1)
    def add_to_back(self, item):
        self._insert_between(item, next=self._head, previous=self._head.previous)

    # O(1)
    def remove_back(self):
        if self.is_empty():
            raise ValueError("List is empty")

        return self._remove_node(self._head.previous)

    # O(1)
    def remove_front(self):
        if self.is_empty():
            raise ValueError("List is empty")

        return self._remove_node(self._head.next)

    # O ( k )
    def pop(self, index):
        if not (0 <= index < self._number_of_items):
            raise IndexError("invalid index")

        current_item = self._head.next

        for number in range(index):
            current_item = current_item.next

        return self._remove_node(current_item)

    # O ( k )
    def insert(self, index, item):
        if not (0 <= index < self._number_of_items):
            raise IndexError("invalid index")

        current_item = self._head.next

        for number in range(index):
            current_item = current_item.next

        self._insert_between(item, previous=current_item.previous, next=current_item)

    def __iter__(self):
        current = self.first()
        while current is not None:
            yield current.data()
            current = self.after(current)

    def _insert_between(self, item, previous, next):
        new_node = self.Node(item, next=next, previous=previous)
        new_node.previous.next = new_node
        new_node.next.previous = new_node

        self._number_of_items += 1

        return new_node

    def _remove_node(self, current_item):
        data = current_item.data
        current_item.data = None
        current_item.previous.next = current_item.next
        current_item.next.previous = current_item.previous
        self._number_of_items -= 1
        return data

    def _validate(self, position):
        if not isinstance(position, self.Position):
            raise TypeError()
        if position._container is not self:
            raise ValueError()
        if position._node.next is None:
            raise ValueError
        return position._node

    def _make_position(self, node):
        if node is self._head:
            return None
        return self.Position(self, node)

    class Node:

        def __init__(self, data, next=None, previous=None):
            self.data = data
            self.next = next
            self.previous = previous


class SinglyLinkedList:

    def __init__(self):
        self._head = None  # front
        self._tail = None  # back
        self._number_of_items = 0

    def __len__(self):
        return self._number_of_items

    def add_to_front(self, data):
        new_node = self.Node(data, self._head)
        self._head = new_node

        if self._head.next is None:
            self._tail = new_node

        self._number_of_items += 1

    def add_to_back(self, data):
        new_node = self.Node(data, None)
        if self._tail is None:
            self._tail = new_node
            self._head = new_node
        else:
            self._tail.next = new_node

        self._number_of_items += 1

    def front(self):
        if self._number_of_items == 0:
            raise ValueError("List is empty")

        return self._head.data

    def remove_front(self):
        if self._number_of_items == 0:
            raise ValueError("List is empty")

        data = self._head.data

        self._head.data = None  # cleanup for garbage collection
        self._head = self._head.next

        if self._head is None:
            self._tail = None

        self._number_of_items -= 1

        return data

    # O ( k )
    def get(self, index):
        if not (0 <= index < self._number_of_items):
            raise IndexError("invalid index")
        current_item = self._head

        for number in range(index):
            current_item = current_item.next

        return current_item.data

    # O ( k )
    def pop(self, index):
        if not (0 <= index < self._number_of_items):
            raise IndexError("invalid index")

        if index == 0:
            return self.remove_front()
        else:
            current_item = self._head

            for number in range(index-1):
                current_item = current_item.next

            data = current_item.next.data
            current_item.next.data = None
            current_item.next = current_item.next.next
            self._number_of_items -= 1

            # check for new tail
            if current_item.next is None:
                self._tail = current_item

            return data

    # O ( index ) - no shifting of items after the index
    def add_to_index(self, index, item):
        if not (0 <= index <= self._number_of_items):
            raise IndexError("invalid index")
        if index == 0:
            self.add_to_front(item)
        elif index == self._number_of_items:
            self.add_to_back(item)
        else:
            current_item = self._head

            for number in range(index-1):
                current_item = current_item.next

            new_item = self.Node(item, current_item.next)
            current_item.next = new_item
            self._number_of_items += 1

    # O ( k ) - no shifting of items after the removed item to 'fill' an empty spot
    def remove(self, item):
        if self._number_of_items == 0:
            raise ValueError("List is empty")
        if self._head.data == item:
            self.remove_front()
        else:
            current = self._head
            while current.next is not None:
                if current.next.data == item:
                    # clears the reference for garbage collection
                    current.next.data = None
                    # jump it in the list
                    current.next = current.next.next
                    self._number_of_items -= 1

                    # check for new tail
                    if current.next is None:
                        self._tail = current

                current = current.next
            else:
                raise ValueError("Item not found!")


    class Node:

        def __init__(self, data, next=None):
            self.data = data
            self.next = next


class LLStack:

    def __init__(self):
        self._data = SinglyLinkedList()

    def __len__(self):
        return len(self._data)

    def push(self, item):
        self._data.add_to_front(item)

    def peek(self):
        return self._data.front()

    def pop(self):
        return self._data.remove_front()


class LLQueue:

    def __init__(self):
        self._data = SinglyLinkedList()

    def __len__(self):
        return len(self._data)

    def front(self):
        return self._data.front()

    def enqueue(self, data):
        self._data.add_to_back(data)

    def dequeue(self):
        return self._data.remove_front()


doublyLinkedList = DoublyLinkedList()

for n in range(10):
    doublyLinkedList.add_to_back(n)

# using the iterator
for item in doublyLinkedList:
    print(item)


# our iteration using position
current_position = doublyLinkedList.first()

while current_position is not None:
    print(current_position.data())
    current_position = doublyLinkedList.after(current_position)