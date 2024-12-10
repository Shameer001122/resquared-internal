import pandas as pd
from jinja2 import Environment, FileSystemLoader
import os

# Load CSV
csv_file = r"C:\\Users\\ST\\OneDrive\\Desktop\\Resquared\\data.csv"
try:
    data = pd.read_csv(csv_file, encoding="utf-8")
except UnicodeDecodeError:
    print("UTF-8 decoding failed, trying ISO-8859-1...")
    data = pd.read_csv(csv_file, encoding="ISO-8859-1")

print(data.head())  # Debug: Print data to ensure correct loading

# Jinja2 Environment
template_dir = r"C:\\Users\\ST\\OneDrive\\Desktop\\Resquared\\templates"
output_dir = r"C:\\Users\\ST\\OneDrive\\Desktop\\Resquared\\output"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

env = Environment(loader=FileSystemLoader(template_dir))
template = env.get_template("index.html")

# Generate HTML Files
for index, row in data.iterrows():
    print(row)  # Debug: Print each row
    try:
        html_content = template.render(
            company_name=row["Name"],
            company_category=row["Categories"],
            address=row["Address"],
            phone=row["Phone"]
        )
        filename = os.path.join(output_dir, f"page_{index + 1}.html")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"Generated: {filename}")
    except Exception as e:
        print(f"Error processing row {index}: {e}")
