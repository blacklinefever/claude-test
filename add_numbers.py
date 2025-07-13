import csv
import os
from datetime import datetime
import duckdb

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

def log_calculation_to_duckdb(numbers, total):
    # Connect to MotherDuck cloud database
    # Falls back to local file if MotherDuck connection fails
    try:
        conn = duckdb.connect('md:')
        db_name = "MotherDuck cloud"
    except Exception:
        # Fallback to local database
        db_file = "calculations.duckdb"
        conn = duckdb.connect(db_file)
        db_name = "local DuckDB"
    
    with conn:
        # Create table with columns for up to 10 numbers
        max_numbers = 10
        number_columns = ', '.join([f'number{i+1} DOUBLE' for i in range(max_numbers)])
        
        conn.execute(f"""
            CREATE TABLE IF NOT EXISTS calculations (
                timestamp TIMESTAMP,
                {number_columns},
                sum DOUBLE
            )
        """)
        
        # Add auto-incrementing id using row_number
        conn.execute("""
            CREATE OR REPLACE VIEW calculations_with_id AS
            SELECT ROW_NUMBER() OVER (ORDER BY timestamp) as id, *
            FROM calculations
        """)
        
        # Prepare the row data (exclude id, let DuckDB auto-increment)
        timestamp = datetime.now()
        row_data = [timestamp] + list(numbers) + [None] * (max_numbers - len(numbers)) + [total]
        
        # Create column list and placeholders for INSERT
        columns = ['timestamp'] + [f'number{i+1}' for i in range(max_numbers)] + ['sum']
        placeholders = ', '.join(['?'] * len(row_data))
        
        conn.execute(f"""
            INSERT INTO calculations ({', '.join(columns)}) VALUES ({placeholders})
        """, row_data)
        
        return db_name

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
        db_location = log_calculation_to_duckdb(numbers, total)
        print(f"Calculation saved to calculations.csv and {db_location}")
    else:
        print("No numbers were entered.")

if __name__ == "__main__":
    main()