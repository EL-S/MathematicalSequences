numbers = []

num = "0"

def get_next_number(number):
    length = len(number)
    last_digit = int(number[-1])
    frequency = 0
    for digit in number:
        if digit == str(last_digit):
            frequency += 1
    #print("freq",frequency)
    next_number = length+frequency
    number += str(next_number)
    numbers.append(next_number)
    print(next_number)
    return number

while True:
    num = get_next_number(num)
    #print("num",num)
