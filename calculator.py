def calculator():
    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        return x / y

    def wholeDiv(x, y):
        return x // y


    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Whole Division")

    while True:
        i = input("Enter choice(1/2/3/4/5): ")

        if i in ('1', '2', '3', '4', '5'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if i == '1':
                print(num1, "+", num2, "=", add(num1, num2))

            elif i == '2':
                print(num1, "-", num2, "=", subtract(num1, num2))

            elif i == '3':
                print(num1, "*", num2, "=", multiply(num1, num2))

            elif i == '4':
                print(num1, "/", num2, "=", divide(num1, num2))

            elif i == '5':
                print(num1, "//", num2, "=", wholeDiv(num1, num2))
        else:
            print("Invalid Input")
