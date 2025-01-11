def print_hello_n_times(n: int):
    """Prints 'Hello, World!' n times.

    Args:
        n (int): The number of times to print the message.
    """
    for i in range(n):
        print('Hello, World!')

def main():
    while True:
        try:
            user_input = int(input('Enter a positive integer: '))
            if user_input <= 0 or user_input > 24:
                print('Please enter a positive integer that is less than 25.\n')
                continue
            print_hello_n_times(user_input)
            break
        except ValueError:
            print('Invalid input. Please enter an integer.\n')

if __name__ == "__main__":
    main()
