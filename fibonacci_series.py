# Program to display the Fibonacci sequence up to given input value

import sys

input = int(sys.argv[1])

# Initial values
n1, n2 = 0, 1
count = 0
# Array to append the values
capture = []

# if condition to validate the parameter passed in an integer
if input <= 0:
   print("Please enter a number greater than Zero or positive integer")
# Condition if the input parameter is 1
elif input == 1:
   print(n1)
# Actions to perform the fibonacci calculation
else:
   while count < input:
       capture.append(n1)
       sum = n1 + n2
       n1 = n2
       n2 = sum
       count += 1
       final_print = n1
final_fib_value = ','.join(map(str, capture)) # Converts the array to string with comma seperated
print("Fibonacci sequence: " + final_fib_value) # Prints the sequence
