import matplotlib.pyplot as plt 

import time 
import sys

def compute_time_to_add(list_to_add, item):
    start = time.perf_counter()
    list_to_add.append(item)
    end = time.perf_counter()
    return end - start 


def compute_time_to_remove(list_to_remove, index):
    start = time.perf_counter()
    list_to_remove.pop(index)
    end = time.perf_counter()
    return end - start 

def compute_time_to_insert(list_to_insert, index):
    start = time.perf_counter()
    list_to_remove.insert(index,index)
    end = time.perf_counter()
    return end - start 


"""
timing = []

my_list= []

values = range(10_000_000)

for n in values:
    timing.append(compute_time_to_add(my_list, n))
"""

timing= []
values = list(range(100_000))
size = []
memory = []
for n in range(len(values)):
    size.append(len(values))
    timing.append(compute_time_to_remove(values,0))
    memory.append(sys.getsizeof(values))

plt.plot(size,timing)
plt.show()
plt.plot(size,memory)
plt.show()