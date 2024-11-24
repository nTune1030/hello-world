def print_hello_n_times(n):
  """Prints 'Hello, World!' n times.

  Args:
    n: The number of times to print the message.
  """

  for _ in range(n):
    print('Hello, World!')

while True:
  try:
    user_input = int(input('Enter a positive integer: '))
    if user_input <= 0:
      print('Please enter a positive integer.\n')
      continue
    print_hello_n_times(user_input)
    break
  except ValueError:
    print('Invalid input. Please enter an integer.\n')
