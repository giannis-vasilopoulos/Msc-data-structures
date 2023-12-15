import csv

# Specify the path for the input CSV file
input_csv_path = './dataset/clean_total_deaths_for_greece_per_date.csv'

# Specify the target column headers
target_column_headers = ['date', 'Greece']

# Read the input CSV file and find the pair with the biggest difference
max_difference = float('-inf')
previous_value = None
max_difference_row = None  # Initialize max_difference_row outside the loop

with open(input_csv_path, 'r', newline='') as input_file:
    csv_reader = csv.DictReader(input_file)

    # Iterate through rows and find the max difference
    for row in csv_reader:
        date = row['date']
        current_value_str = row['Greece']

        # Skip non-numeric values or empty strings
        if current_value_str:
            try:
                current_value = int(current_value_str)
            except ValueError:
                continue  # Skip if conversion to int fails

            if previous_value is not None:
                current_difference = current_value - previous_value
                if current_difference > max_difference:
                    max_difference = current_difference
                    max_difference_row = {'date': date, 'Greece': current_value}

            previous_value = current_value

# Display the result
if max_difference_row:
    print(f"The row with the biggest difference is: {max_difference_row}")
    print(f"The biggest difference is: {max_difference}")
    print(f"Raw numbers: {max_difference_row['Greece']} and {previous_value}")
else:
    print("No consecutive rows found.")
