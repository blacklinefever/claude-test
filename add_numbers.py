import csv
import os
from datetime import datetime

def log_calculation_to_csv(numbers, total):
    csv_file = "calculations.csv"
    file_exists = os.path.exists(csv_file)
    
    # Determine the maximum number of columns needed
    max_numbers = 10  # Allow up to 10 numbers by default
    if file_exists:
        # Check existing file to see if we need more columns
        with open(csv_file, mode='r') as file:
            reader = csv.reader(file)
            headers = next(reader, [])
            if headers:
                # Count existing number columns (exclude Timestamp and Sum)
                number_cols = len([h for h in headers if h.startswith('Number')])
                max_numbers = max(max_numbers, number_cols, len(numbers))
    else:
        max_numbers = max(max_numbers, len(numbers))
    
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        
        if not file_exists:
            headers = ['Timestamp'] + [f'Number{i+1}' for i in range(max_numbers)] + ['Sum']
            writer.writerow(headers)
        
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        row = [timestamp] + list(numbers) + [''] * (max_numbers - len(numbers)) + [total]
        writer.writerow(row)

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