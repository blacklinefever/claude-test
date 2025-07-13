def main():
    print("Welcome to the Number Addition Calculator!")
    print("This program will add together all the numbers you enter.")
    print()
    
    numbers = []
    
    print("Please enter the numbers you want to add together:")
    print("(Press Enter without typing a number when you're finished)")
    
    while True:
        user_input = input("Enter a number: ").strip()
        
        if not user_input:
            break
            
        try:
            number = float(user_input)
            numbers.append(number)
            print(f"Added {number} to the list")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    if numbers:
        total = sum(numbers)
        print(f"\nCalculation complete!")
        print(f"Numbers entered: {numbers}")
        print(f"Sum: {total}")
    else:
        print("No numbers were entered.")

if __name__ == "__main__":
    main()