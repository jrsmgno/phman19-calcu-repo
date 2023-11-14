def calculate():
    try:
        # Get the number of values for the mathematical operation
        num_values = int(input('How many numbers do you want to use for the operation? '))

        # Validate the number of values
        if num_values < 2:
            print('Please enter at least two numbers for the operation.')
            return

        # Get the math operation from the user
        operation = input('''
    Please type in the math operation you would like to complete:
    + for addition
    - for subtraction
    * for multiplication
    / for division
    ''')

        # Get the numbers from the user based on the number of values
        numbers = [float(input('Please enter number {}: '.format(i + 1))) for i in range(num_values)]

        result = perform_operation(operation, numbers)

        if result is not None:
            print('Result:', result)

    except ValueError:
        print('Invalid input. Please enter numerical values.')

    except ZeroDivisionError:
        print('Error: Division by zero is not allowed.')

    # Ask if the user wants to calculate again
    again()

def perform_operation(operation, numbers):
    result = numbers[0]

    for i in range(1, len(numbers)):
        if operation == '+':
            result += numbers[i]
        elif operation == '-':
            result -= numbers[i]
        elif operation == '*':
            result *= numbers[i]
        elif operation == '/':
            if numbers[i] == 0:
                raise ZeroDivisionError
            result /= numbers[i]
        else:
            print('Invalid operator')
            return None

    return result

def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('See you again!')
    else:
        again()

# Start the calculation
calculate()
