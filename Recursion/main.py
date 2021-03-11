import matplotlib.pyplot as plt
import progression

first = progression.Progression()

count = 0 

#we can iter over the class thanks to the magic method __iter__.
"""
for value in first:
    count+=1
    print(value)
    if count == 100:
        break
"""

second = progression.Progression()

#if we write next here, we can avoid using the __iter__.
"""for n in range(100):
    print(next(second))"""

"""
r_value = float(input('Please enter an input: '))


geo = progression.GeometricProgression(r_value)
current_sum = 0
expected_value = 1/(1-r_value)

while abs(expected_value - current_sum) > 0.000001:
    current_sum += next(geo)
    print(current_sum)
"""

fib =progression.FibonacciProgresion()
next(fib) # progress on the initial 0

digit_count = {}
for digit in range(1,10):
    digit_count[digit]=0

for value in range(500):
    fib_value = next(fib)
    string_fib_value = str(fib_value)
    leading_digit = int(string_fib_value[0])
    digit_count[leading_digit] += 1

print(digit_count)

plt.figure()
plt.plot(list(digit_count.keys()), list(digit_count.values()))
plt.show()
