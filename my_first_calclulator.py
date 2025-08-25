
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number, root or power: "))
operator = input("Enter operator: ")


def raise_to_power(base, exponent):
    result = 1
    for index in range(exponent):
        result = result * base
    return result

def power_root(num1, num2):
    result = num1 ** (1/num2)
    return result


if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    try:
        print(num1 / num2)
    except ZeroDivisionError as err:
        print("You can't divide by zero!")
elif operator == "^":
    print(num1 ** num2)
    #print(raise_to_power(int(num1), int(num2)))
elif operator == "root":
    print(power_root(int(num1), int(num2)))
elif operator == "%":
    print(num1 % num2)
else:
    print("Invalid operator")

