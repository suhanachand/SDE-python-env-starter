### This simple calculator program can add, subtract, multiply and divide two numbers/integers


############ FUNCTIONS DEFINITIONS ###############################


#adding two integers
def add(a, b):
  c = a + b
  print(f'{a} + {b} = {c}')


#subtracting two integers
def sub(a, b):
  c = a - b
  print(f'{a} - {b} = {c}')


# multiplying two integers
def multiply(a, b):
  c = a * b
  print(f'{a} x {b} = {c}')


#dividing two integers
def divide(a, b):
  if b != 0:
    c = a / b
    print(f'{a} / {b} = {c}')
  else:
    print(" cannot divide by zero.")


#The calcultor function
def calculator(a, b, ops):
  if ops == 1:
    add(a, b, ops)
  elif ops == 2:
    sub(a, b, ops)
  elif ops == 3:
    multiply(a, b, ops)
  elif ops == 4:
    divide(a, b, ops)


#displaying the calculator menu
def menu_display():
  print("""
      ----------------
      Calculator Menu
      ----------------
      1 - Add
      2 - Subtract
      3 - Multiply
      4 - Divide
      """)

#user entries validation function
def user_selection():
  try:
    ops = int(input("Enter your Choice of Operation(1-4): "))
  except ValueError:
    ops = 0

  try:
      a = int(input("Enter the first number: "))
  except ValueError:
      b = -1000000000000

  try:
      b = int(input("Enter the second number: "))
  except ValueError:
      b = -1000000000000

  if ops<1 or ops>4 or a ==-1000000000000 or b==-1000000000000:
    print("Sorry, one of the entries was not right.")
  else:
   calculator(a, b, ops)

############ Main Function ###############################
def main():
  menu_display()
  user_selection()

if __name__ == "__main__":
  main()
