class Input_Value:
    #If the value is number (int, float)
    def isNumber(self,input):
        try:
            float(input)
            return True
        except ValueError:
            return False

    def isInt(self,input):
        try:
            int(input)
            return True
        except ValueError:
            return False

#check the value of option input
def check_option(value, low, high):
    p = Input_Value()
    while not p.isInt(value) or int(value) < low or int(value) > high:
        print("\nThe option should be a integer number between " + str(low) + " and " + str(high) + "!")
        print("Try again for your option!\n")
        value = input("Your selection: ")
        
    return value