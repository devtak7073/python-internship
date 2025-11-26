while True:
    print( """
          1: Addition
          2: Subtraction 
          3: Multiplication
          4: cm to metre conversion
          5: Celcius to fahrenheit 
          6: Division
          7: Exit 
          """)
    choice = input("Enter your choice:")

    if choice == "1":
        num1 = int (input("Enter first number "))
        num2 = int (input("Enter second number"))
        print("Addition is: ", num1 + num2)

    elif choice == "2":
        num1 = int (input("Enter  first number "))
        num2 = int (input("Enter second number"))
        print("Subtraction is: ", num1 - num2)
    elif choice == "3":
        num1 = int (input("Enter first number "))
        num2 = int (input("Enter second number"))
        print("Product is: ", num1 * num2)
    elif choice == "4":
        num1 = float (input("Enter number "))
        print("cm to M conversion is: ",num1/100)
    elif choice == "5":
        num1 = float (input("Enter temperature in celcius "))
        fahrenheit=(num1 * 9/5)+32
        print("temperature in fahrenheit is ",fahrenheit)
    elif choice == "6":
        num1 = int (input("Enter first number "))
        num2 = int (input("Enter second number"))
        print("Division is: ", num1 / num2)
    elif choice == "7":
        print("Exiting the program...") 
        break 
    else : 
         print("Invalid")