
def CheckPasswordStrength():
    password = str(input("please input a password!"))
    lengthValue = CheckPasswordLength(password)
    strength = CheckPasswordCharacters(lengthValue, password)


    '''''''''''
    I will add values to the password and then divide to keep a base 5.
    5. Excellent
    4. Good
    3.Decent
    2. subpar
    1.Terrible
    '''''''''''

def CheckPasswordLength(password):
    if len(password) >= 14:
        lengthValue =5

    if len(password) <14 and len(password)>=12:
        lengthValue =4

    if len(password) < 12 and len(password) >= 10:
        lengthValue =3

    if len(password) < 10 and len(password) >= 8:
        lengthValue =2
    if len(password) <=7:
        lengthValue =1

    return lengthValue

def CheckPasswordCharacters(lengthValue, password):
    upperValue = float(0)
    lowerValue = float(0)
    numberValue = float(0)
    symbolValue = float(0)

    upperCount = int(0)
    numberCount = int(0)
    symbolCount = int(0)
    lowerCount = int(0)
    for element in range (0, len(password)):
        if password[element].islower():
            lowerCount = lowerCount+1

        if password[element].isupper():
            upperCount = upperCount+1

        if password[element].isdigit():
            numberCount = numberCount+1

        if not password[element].isalnum():
            #character is a symbol
            symbolCount = symbolCount+1

    if upperCount > 2:
        upperValue = 1
    if lowerCount >= 8:
        lowerValue =1
    if numberCount >=2:
        numberValue =1
    if symbolCount >=1:
        symbolValue = 1

    final = (upperValue + lowerValue +numberValue + symbolValue+ lengthValue)/2
    print("your password has a strength of ")
    if final <= 0.5:
        print('terrible')

    if final>= 1 and final<2:
        print('subpar')
    if final>=2 and final<3:
        print ("decent")
    if final >=3 and final <4:
        print('good')
    if final >=4 and final <5:
        print('Excellent!')
    print("\033[0m")
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while True:
        CheckPasswordStrength()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/






