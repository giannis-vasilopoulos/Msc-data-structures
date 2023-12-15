import csv

# Specify the paths for input and output CSV files
input_csv_path = './dataset/raw_covid_total_deaths_per_date.csv'
output_csv_path = './dataset/clean_total_deaths_for_greece_per_date.csv'

# Specify the target columns' headers
target_column_headers = ['date', 'Greece']

# Read the input CSV file and filter columns
with open(input_csv_path, 'r', newline='') as input_file:
    csv_reader = csv.DictReader(input_file)

    # Get the fieldnames (headers) from the input file
    fieldnames = csv_reader.fieldnames

    # Filter only the rows with the target columns and write to the output CSV file
    with open(output_csv_path, 'w', newline='') as output_file:
        csv_writer = csv.DictWriter(output_file, fieldnames=target_column_headers)

        # Write the header
        csv_writer.writeheader()

        # Write the filtered columns directly without using rows_to_keep
        for row in csv_reader:
            filtered_row = {header: row[header] for header in target_column_headers}
            csv_writer.writerow(filtered_row)





#The overall time complexity of the code is O(n)