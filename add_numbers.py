import csv
import os
from datetime import datetime

def log_calculation_to_csv(numbers, total):
    csv_file = "calculations.csv"
    file_exists = os.path.exists(csv_file)
    
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        
        if not file_exists:
            writer.writerow(['Timestamp', 'Numbers', 'Sum'])
        
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        numbers_str = ', '.join(map(str, numbers))
        writer.writerow([timestamp, numbers_str, total])

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
        
        log_calculation_to_csv(numbers, total)
        print("Calculation saved to calculations.csv")
    else:
        print("No numbers were entered.")

if __name__ == "__main__":
    main()