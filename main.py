from gui import start_gui
from calculator import perform_operation
from timer import countdown_timer

def main():
    print("Welcome to Countdown Timer & Calculator App")
    choice = input("Run GUI? (y/n): ").lower()
    if choice == 'y':
        start_gui()
    else:
        while True:
            print("\n1. Countdown Timer\n2. Calculator\n3. Exit")
            opt = input("Choose an option: ")
            if opt == '1':
                try:
                    seconds = int(input("Enter seconds for countdown: "))
                    countdown_timer(seconds)
                except ValueError:
                    print("Please enter a valid number.")
            elif opt == '2':
                a = input("Enter first number: ")
                op = input("Enter operator (+, -, *, /): ")
                b = input("Enter second number: ")
                result = perform_operation(a, b, op)
                print(f"Result: {result}")
            elif opt == '3':
                break
            else:
                print("Invalid choice.")

if __name__ == "__main__":
    main()