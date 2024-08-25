class Calculator:

    error_zero = "Opps!. Divide by zero"

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def add(self):
        return self.num1 + self.num2
    
    def substract(self):
        return self.num1 - self.num2
    
    def multiply(self):
        return self.num1 * self.num2
    
    def divide(self):
        if(self.num2 == 0): raise Exception(self.error_zero)
        return self.num1/self.num2
    
    def mod(self):
        if(self.num2 == 0): raise Exception(self.error_zero)
        return self.num1%self.num2

def main():
    try:    
        while True:

            option = int(input("--> Enter 1 to add \n--> Enter 2 to substract \n--> Enter 3 to multiply \n--> Enter 4 to divide \n--> Enter 5 to mod \n--> Enter 6 to exit \n"))

            if option == 1 or option == 2 or option == 3 or option == 4 or option == 5:
                num1 = float(input("\nEnter the first number: "))
                num2 = float(input("Enter the second number: "))

                calculator_machine = Calculator(num1, num2)

                if(option == 1): print(f"The addition between {num1} and {num2} is {calculator_machine.add()}\n")
                if(option == 2): print(f"The substraction between {num1} and {num2} is {calculator_machine.substract()}\n")
                if(option == 3): print(f"The multiplication between {num1} and {num2} is {calculator_machine.multiply()}\n")
                if(option == 4): print(f"The division between {num1} and {num2} is {calculator_machine.divide()}\n")
                if(option == 5): print(f"The modulo operation between {num1} and {num2} is {calculator_machine.mod()}\n")
            
            elif option == 6: break
            else: print("Wow!. Wrong option :(. Enter a correct value\n")


    except Exception as err:
        print(err)

if __name__ == "__main__":
    main()
