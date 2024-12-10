import csv
import os
import re  # For sanitizing file names

# Paths to your files and directories
csv_file = 'C:\\Users\\ST\\OneDrive\\Desktop\\Resquared\\data.csv'  # Path to your CSV file
html_template_file = 'C:\\Users\\ST\\OneDrive\\Desktop\\Resquared\\templates\\index.html'  # Corrected path to your HTML template file
output_dir = 'C:\\Users\\ST\\OneDrive\\Desktop\\Resquared\\output'  # Output directory for generated HTML files

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Function to sanitize file names
def sanitize_filename(name):
    """Remove invalid characters and replace spaces with underscores."""
    name = re.sub(r'[<>:"/\\|?*\x00-\x1F]', '', name)  # Remove invalid characters
    return name.strip().replace(' ', '_')  # Replace spaces with underscores

# Read the HTML template file
try:
    with open(html_template_file, 'r', encoding='utf-8') as template_file:
        html_template = template_file.read()
except FileNotFoundError:
    print(f"Error: The HTML template file '{html_template_file}' does not exist.")
    exit()

# Read data from the CSV file and generate HTML files
try:
    with open(csv_file, 'r', encoding='latin-1') as csvfile:  # Use latin-1 encoding to handle special characters
        csv_reader = csv.DictReader(csvfile)

        # Check available column headers in the CSV file
        csv_headers = csv_reader.fieldnames
        print(f"CSV Headers: {csv_headers}")  # Debugging step to verify headers

        for row in csv_reader:
            # Replace placeholders in the template with data from the CSV
            output_html = html_template
            for key, value in row.items():
                placeholder = f'{{{{ {key} }}}}'  # Placeholder format {{ key }}
                output_html = output_html.replace(placeholder, value)

            # Use a valid column name from your CSV for the file name
            if 'company_name' in row:
                raw_file_name = row['company_name']
                file_name = sanitize_filename(raw_file_name)  # Sanitize the file name
            else:
                raise KeyError("Required column for naming files ('company_name') is missing in CSV.")

            # Generate the output file path and write the HTML file
            output_file_path = os.path.join(output_dir, f"{file_name}.html")
            with open(output_file_path, 'w', encoding='utf-8') as output_file:  # Save output with utf-8 encoding
                output_file.write(output_html)

    print("HTML pages generated successfully!")
except FileNotFoundError:
    print(f"Error: The CSV file '{csv_file}' does not exist.")
except KeyError as e:
    print(f"Error: Missing key in CSV data: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
