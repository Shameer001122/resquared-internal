import pandas as pd
from jinja2 import Environment, FileSystemLoader
import os

# Step 1: Load the CSV file
csv_file = "C:\\Users\\ST\\OneDrive\\Desktop\\Resquared\\data.csv"  # Replace with the path to your CSV file
data = pd.read_csv(csv_file)

# Step 2: Setup Jinja2 environment
template_dir = "C:\\Users\\ST\\OneDrive\\Desktop\\Resquared\\templates"  # Folder where your HTML template is stored
output_dir = "C:\\Users\\ST\\OneDrive\\Desktop\\Resquared\\output"  # Folder to save generated HTML pages

if not os.path.exists(output_dir):  # Create output folder if it doesn't exist
    os.makedirs(output_dir)

env = Environment(loader=FileSystemLoader(template_dir))
template = env.get_template("index.html")  # Your HTML template name

# Step 3: Generate HTML files
for index, row in data.iterrows():
    # Render template with CSV data
    html_content = template.render(
        title=row["Name"],       # Replace with your CSV column names
        header=row["Address"],     # Replace with your CSV column names
        description=row["City"]  # Replace with your CSV column names
    )
    
    # Save to individual HTML files
    filename = os.path.join(output_dir, f"page_{index + 1}.html")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Generated: {filename}")
