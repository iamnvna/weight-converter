print("Welcome to weight converter!"
      "\nConvert from Pounds to Kilograms and vice versa.")

weight = 0
convert = 0
first_weight = input("\nWhich weight option are you converting from? K/P: ").lower()

while True:
      if first_weight not in ['k', 'p']:
            print("Enter a valid option.")
      else:
            weight = float(input("Enter the weight value: "))

      if first_weight == 'k':
            convert = (weight * 2.2046)
            print(weight, "pounds converts to", convert, "kilograms.")
            break
      else:
            convert = (weight / 2.2046)
            print(weight, "kilograms converts to", convert, "pounds.")
            break




