
import numpy as np
numbers = np.array([250, 300, 200, 400, 150, 500, 350])

print(numbers[1])
print(numbers[4])
print(numbers[6])
print(numbers[2:6])
print(numbers[2:6:2])

print("Total:", np.sum(numbers))
print("Minimum:", np.min(numbers))
print("Maximum:", np.max(numbers))
print("Mean:", np.mean(numbers))
print("Standard Deviation:", np.std(numbers))

increased = numbers*1.10
print("after 10% increase:", increased)

reduced= numbers-40
print("After reducing 40:", reduced)

high=numbers[numbers>250]
print("Higher than 250:",high)

low=numbers[numbers<250]
print("Lower than 250:",low)

for number in numbers:
    if number>250:
        print(number)

matrix=numbers.reshape(7,1)
print(matrix)