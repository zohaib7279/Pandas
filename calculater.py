
print('------ Calculator ------')

a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

operations = input('Enter operation (+, -, *, /): ')

if operations == '+':
    print('Ruselt: a+b')
elif operations == '-':
    print('Ruselt: a-b')
elif operations == '*':
    print('Ruselt: a*b')
elif operations == '/':
    if b != 0:
        print('Ruselt: a/b')
    else:
        print('Error: Division by zero is not allowed.')