import re
def preprocess_expression(expression):
    expression = expression.replace('×', '*').replace('÷', '/')
    expression = re.sub(r'(\d+|\))\s*(\()', r'\1*\2', expression)
    return expression
def dynamic_calculator(expression):
    processed_expression = preprocess_expression(expression)
    try:
        result = eval(processed_expression)
        return result
    except Exception as e:
        return f"Error: {e}"
def main():
    print("Welcome to the Dynamic Calculator!")
    print("Type 'exit' to quit.")
    while True:
        user_input = input("Enter an expression: ")
        if user_input.lower() == 'exit':
            print("Exiting the calculator. Goodbye!")
            break
        result = dynamic_calculator(user_input)
        print("Result:", result)
if __name__ == "__main__":
    main()
