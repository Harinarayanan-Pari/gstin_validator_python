# import csv
# import re

# # Function to classify GST type using regular expressions
# def classify_gst_type(gst_number):
#     pattern = r'^\d{2}[A-Z]{5}\d{4}[A-Z]\d[Z1-9A-Z]{3}$'
#     if re.match(pattern, gst_number):
#         check_digit = gst_number[-1]
#         if check_digit in ['Z', 'A', 'B'] or check_digit.isdigit() or check_digit in ['E', 'F', 'G', 'H', 'I', 'J']:
#             return "Normal, Composite, Casual"
#         elif check_digit == 'S':
#             return "Input Service Distributor"
#         elif check_digit == 'C':
#             return "Tax Collector"
#         elif check_digit == 'D':
#             return "Tax Deductor"
#         else:
#             return "Invalid GSTIN"
#     else:
#         return "Invalid GSTIN"

# # Function to process CSV
# def process_csv(input_file, output_file):
#     with open(input_file, 'r') as csvfile:
#         reader = csv.reader(csvfile)
#         next(reader)  # Skip header row
#         gstin_list = [row[0] for row in reader if row]  # Extract GSTIN numbers from CSV
    
#     # Classify GST types
#     classified_data = [{'GSTIN': gstin, 'FORMAT': classify_gst_type(gstin)} for gstin in gstin_list]

#     # Write the classified data to a new CSV file
#     with open(output_file, 'w', newline='') as csvfile:
#         fieldnames = ['GSTIN', 'FORMAT']
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#         writer.writeheader()
#         writer.writerows(classified_data)

# # Input and output file paths
# input_file = 'output.csv'  # Replace with the path to your input CSV file
# output_file = 'out.csv'  # Path to save the output CSV file

# # Process the CSV file
# process_csv(input_file, output_file)

# print("CSV processing complete. Check output file for the result.")

import csv
import re

# Function to classify GST type using regular expressions
def classify_gst_type(gst_number):
    pattern = r'^\d{2}[A-Z]{5}\d{4}[A-Z]\d[Z1-9A-Z]{3}$'
    if re.match(pattern, gst_number):
        check_digit = gst_number[-1]
        if check_digit in ['Z', 'A', 'B'] or check_digit.isdigit() or check_digit in ['E', 'F', 'G', 'H', 'I', 'J']:
            return "Normal, Composite, Casual"
        elif check_digit == 'S':
            return "Input Service Distributor"
        elif check_digit == 'C':
            return "Tax Collector"
        elif check_digit == 'D':
            return "Tax Deductor"
        else:
            return " "
    else:
        return " "

# Function to process CSV
def process_csv(input_file, output_file):
    with open(input_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        gstin_list = [row[0] for row in reader if row]  # Extract GSTIN numbers from CSV
    
    # Classify GST types
    classified_data = [{'GSTIN': gstin, 'FORMAT': classify_gst_type(gstin)} for gstin in gstin_list]

    # Write the classified data to a new CSV file
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['GSTIN', 'FORMAT']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(classified_data)

# Input and output file paths
input_file = 'output.csv'  # Replace with the path to your input CSV file
output_file = 'out.csv'  # Path to save the output CSV file

# Process the CSV file
process_csv(input_file, output_file)

print("CSV processing complete. Check output file for the result.")