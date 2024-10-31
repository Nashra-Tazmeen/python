import os
import pdfkit
import subprocess

# Base directory containing the HTML files
base_dir = 'Data/Html_Data'
# Output directory for PDFs
output_dir = 'new_pdfs'

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Loop through each year from 2019 to 2023
for year in range(2008, 2024):
    year_folder = os.path.join(base_dir, str(year))
    
    # Ensure the year folder exists
    if os.path.exists(year_folder):
        # Loop through each month from 1 to 12
        for month in range(1, 13):
            # Construct the path for the HTML file
            html_file_path = os.path.join(year_folder, f'{month}.html')  # Path to the HTML file
            output_pdf_path = os.path.join(output_dir, str(year), f'{month}.pdf')  # Path for the output PDF
            
            # Ensure the year subdirectory in output_dir exists
            os.makedirs(os.path.dirname(output_pdf_path), exist_ok=True)

            # Check if the HTML file exists before converting
            if os.path.exists(html_file_path):
                # Define options for pdfkit
                options = {
                    'quiet': '',  # Suppresses output
                    'allow': '',  # Allow local file access
                }
                
                try:
                    # Convert HTML to PDF with options
                    pdfkit.from_file(html_file_path, output_pdf_path, options=options)
                    print(f'Successfully converted {html_file_path} to {output_pdf_path}')
                except OSError as e:
                    print(f'Failed to convert {html_file_path}: {e}')
                except Exception as e:
                    print(f'Error during conversion for {html_file_path}: {e}')
            else:
                print(f'HTML file does not exist: {html_file_path}')
    else:
        print(f'Year folder does not exist: {year_folder}')
