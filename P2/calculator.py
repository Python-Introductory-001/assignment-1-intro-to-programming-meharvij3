def add(num1, num2):
    result = 0
    result = num1 + num2
    # Add your addition logic here

    return result

def subtract(num1, num2):
    result = 0
    result = num1 - num2

    # Add your subtraction logic here

    return result

def multiply(num1, num2):
    result = 0
    result = num1 * num2

    # Add your multiplication logic here

    return result

def divide(num1, num2):
    result = 0
    if num2 == 0:
        return "ERROR!"
    else:
        result = num1 / num2
        return result

def calculator(num1, num2, operator, resultType):
    result = 0
    if operator == "+":
        result = add(num1, num2)
    elif operator == "-":
        result = subtract(num1, num2)
    elif operator == "*":
        result = multiply(num1, num2)
    elif operator == "/":
        if num2 == 0:
            return "ERROR!"
        else:
            result = divide(num1, num2)
    if resultType == "f":
        return float(result)
    elif resultType == "i":
        return int(result)
    
    

    # Add conditional (operator) logic here


    # Convert result to specified type (Remember to handle the scenario where division by zero occurs)


    return result
# END OF CODE