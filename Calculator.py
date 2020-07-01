#a = input("Type in something : "))
# print(a)

#Calculator program
# 1 means loop, 0 means don't loop
loop = 1
#Name = input("Please type your name: ")
choice = 0
Name = str(input("Please give us your name: "))
while loop == 1:
    #print options
    print(" ")
    print ("Hello", Name,"welcome to my Calculator Program!")
    print ("Your options are: ")
    print(" ")
    print("1) Addition")
    print("2) Subtraction")
    print("3) Multiplication")
    print("4) Division")
    print("5) Quit")
    print(" ")
   # Name = str(input("Please give us your name: "))
    print("Hello", Name)
    choice = int(input("Choose your option: "))
    if choice == 1:
        A = float(input("Add this: ")) # Float instead of int so we can add compute decimal numbers
        B = float(input("to this: "))
        print("Congrats", Name, "Your Result is: ", A + B )
        print(" ")
    elif choice == 2:
        sub_2= float(input("Subtract this: "))
        sub_1 = float(input("from this: "))    
        print("Congrats", Name, "Your Result is: ", sub_1-sub_2)
    elif choice == 3:
        Mul_1 = float(input("Multiply this: "))
        Mul_2 = float(input("With this: "))
        print("Congrats", Name, "Your Result is: ", Mul_1 * Mul_2)
    elif choice == 4:
        Div_1 = float(input("Divide this: "))
        Div_2 = float(input("By this: "))
        print("Congrats", Name, "Your Result is: ", Div_1 / Div_2)
    elif choice == 5:
        Statement = input("Would you like to quit this program?: ")
        if Statement == "No":
            print("Congrats", Name, "Please Continue")
        else:
            print("Dear", Name, "Thank you for using my Calculator Program")
        loop = 0
    else:
        print("Please input a valid option") # If the user tries to input any other option asides the available ones
        
        print("Thank You")
