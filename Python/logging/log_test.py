import logging
import logging.config



def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x ,y):
    return x * y

def divide(x, y):
    return x / y




#replace print statements with log statements


num_1 = 10
num_2 = 5

add_result = add(num_1, num_2)
print(num_1, num_2, add_result)

sub_result = subtract(num_1, num_2)
print(num_1, num_2, sub_result)


