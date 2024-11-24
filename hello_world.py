def hello_print(user_input):
    for _ in range(user_input):
        print('Hello, World!')

while True:
    user_input = int(input('Enter a number: '))
    if user_input < 1:
        print('Try again\n')
        continue
    hello_print(user_input)
    break
