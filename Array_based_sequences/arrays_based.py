

class Dynamic_Array():

    def __init__(self):
        self._number_of_items = 0
        self._data = [None]

    def __len__(self):
        return self._number_of_items

    def __getitem__(self, index):
        if not 0 <= index < self._number_of_items:
            raise IndexError
        return self._data[index]

    def append(self, item):
        if self._number_of_items == len(self._data):
            new_data = [None] *len(self._data) *2
            for index in range(len(self._data)):
                new_data[index] = self._data[index]
            self._data = new_data
        
        self._data[self._number_of_items] = item
        self._number_of_items += 1


test = Dynamic_Array()

for number in range(10):
    test.append(number)

for index in range(len(test)):
    print(test[index])