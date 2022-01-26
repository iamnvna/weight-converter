print("Welcome to weight converter!"
      "\nConvert from Pounds to Kilograms and vice versa.")

weight = 0
convert = 0

first_weight = input("\nWhich weight option are you converting from? K/P: ").lower()
while True:
    if first_weight not in ['k', 'p']:
        print("Enter a valid option.")
    else:
        try:
            weight = float(input("Enter the weight value: "))
        except ValueError:
            print("Oops! That was no valid number. Try again.")
            break
    
    if first_weight == 'k':
        convert = (weight * 2.2046)
        print(weight, "pounds converts to", convert, "kilograms.")
        break
    else:
        convert = (weight / 2.2046)
        print(weight, "kilograms converts to", convert, "pounds.")
        break

# Commentary
"""
Line 1:
      The print statement welcomes the user to the program, and explains the program
      function.

Line 4-5:
      The variables to hold the weight input from the user and the converted values
      are declared here.

Line 7:
      Line 7 asks for input from the user, the user enters the weight measure they are
      converting from.

Line 8-25:
      while True allows the code block below it rerun anytime it meets the continue
      keyword. The block of code first checks to be sure the user entered either k or p.
      If not, they are prompted to enter a valid input. Where the user entered either
      k or p, the user is further asked to input the weight value to be converted. Error
      handling is employed here to make sure that any other input aside an integer or float
      from the user is thrown as an error and "Oops! That was no valid number. Try again."
      is printed on the screen. The code from line 9 is evaluated against the if statement
      in line 18, and the appropriate code runs.
"""
