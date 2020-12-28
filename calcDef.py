#Chosen = 0

#operation functions
def Ops(a,O,b):
    if O == 1:
        print("Result of", a, "+", b, "is", a + b)
    elif O == 2:
        print("Result of", a, "-", b, "is", a - b)
    elif O == 3:
        print("Result of", a, "*", b, "is", a * b)
    elif O == 4:
        print("Result of", a, "/", b, "is", a / b)
    else:
        print("Invalid input, please try again.")

#showing all the choices
def Choices():
    print("--- Calculator Program ---")
    print("Operations : ")
    print("[1] Add")
    print("[2] Substract")
    print("[3] Multiply ")
    print("[4] Devide")

#inputs & output
def DoIt():
    #input chosen choice (input something, or 0 if its empty)
    Chosen = int(input("Choose one of the operation above : ") or 0) 
    #input for the numbers (input something, or 0 if its empty)
    Num1=float(input("Put in the first number : ") or 0)
    Num2=float(input("Put in the second number : ") or 0)
    #launch Ops
    print("-------------------------------------") #devider maybe?
    Ops(Num1,Chosen,Num2)
    print("-------------------------------------")

def TryAgain():
    try_again = str(input("Try Again? [y/N] " or "n"))
    if try_again == "y" or try_again == "Y" :
        Choices()
        DoIt()
        TryAgain()
    else:
        pass

def main():
    print("Wrong program, please launch calculator.py instead")

if __name__ == "__main__":
    main()
    pass