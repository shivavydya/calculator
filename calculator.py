def perform_operation(a, b, op):
    try:
        a, b = float(a), float(b)
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            return a / b if b != 0 else "Error: Division by zero"
        else:
            return "Invalid operator"
    except ValueError:
        return "Invalid input: Please enter numbers"