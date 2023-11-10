def calculator():
  #addition
  def add(n1, n2):
      return n1 + n2
  #subtraction
  def subtract(n1, n2):
      return n1 - n2
  #multiplication
  def multiply(n1, n2):
      return n1 * n2
  #divide
  def divide(n1, n2):
      return n1 / n2
  operations = {"+": add, "-": subtract, "*": multiply, "/": divide}
  num1 = float(input("First Number: "))
  for operator in operations:
      print(operator)
  should_continue = True
  while should_continue:
    operation_symbol = input("Pick out an operation: ")
    num2 = float(input("Next Number: "))
    calculation_fun = operations[operation_symbol]
    answer = calculation_fun(num1, num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    
    user_input = input("Type 'y' to continue with the result, type 'n' for a new calculation, type 'e' to exit: ")

    if user_input == 'y':
      num1 = answer
    elif user_input == 'n':
      should_continue = False
      calculator()
    else:
      print("Exiting the calculator.")
      should_continue = False

calculator()