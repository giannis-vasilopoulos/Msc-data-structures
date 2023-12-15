import csv

# Specify the path for the input CSV file
input_csv_path = './dataset/clean_total_deaths_for_greece_per_date.csv'

# Specify the target column headers
target_column_headers = ['date', 'Greece']

# Read the input CSV file and find the pair with the biggest difference
max_difference = float('-inf')
previous_row = None

with open(input_csv_path, 'r', newline='') as input_file:
    csv_reader = csv.DictReader(input_file)

    # Iterate through rows and find the max difference
    for row in csv_reader:
        current_date = row['date']
        current_value_str = row['Greece']

        # Skip non-numeric values or empty strings
        if current_value_str:
            try:
                current_value = int(current_value_str)
            except ValueError:
                continue  # Skip if conversion to int fails

            if previous_row is not None:
                previous_date = previous_row['date']
                previous_value = int(previous_row['Greece'])
                current_difference = current_value - previous_value

                if current_difference > max_difference:
                    max_difference = current_difference
                    max_difference_previous_date = previous_date
                    max_difference_previous_value = previous_value
                    max_difference_current_date = current_date
                    max_difference_current_value = current_value

            previous_row = row

# Display the result
if max_difference_previous_date is not None:
    print(f"The previous date and value are: {max_difference_previous_date}, {max_difference_previous_value}")
    print(f"The current date and value are: {max_difference_current_date}, {max_difference_current_value}")
    print(f"The biggest difference is: {max_difference}")
else:
    print("No consecutive rows found.")
