#Code for automating mathematical operations

print('What operation would you like to perform')
operation = int(input('Enter 1 for addition, enter 2 for subtraction, enter 3 for multiplication, enter 4 for division, enter 5 for modulus'))
n1 = int(input('Enter 1st number'))
n2 = int(input('Enter 2nd number'))

if operation == 1 :
    answer = n1 + n2

if operation == 2 :
    answer = n1 - n2

if operation == 3 :
    answer = n1 * n2

if operation == 4 :
    answer = n1 / n2

if operation == 5 :
    answer = n1 % n2

print(answer)
