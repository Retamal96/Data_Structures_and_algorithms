def count(number):
    if number <0: #base case to stop recursion 
        return 
    print(number)
    return count(number-1) #how are we approaching the base case


def fib(nth):
    if nth<2:
        return 1
    return fib(nth-1) + fib(nth-2)

def _better_fib(nth, current_nth, previous, current):
    if nth == current_nth:
        return previous + current
    return _better_fib(nth, current_nth+1, current, previous+ current)

def better_fib(nth):
    if nth <2:
        return 1
    return _better_fib(nth,2,1,1)

for i in range(100):
    print(better_fib(i))