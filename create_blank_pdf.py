import os  # Import os module
import re  # Import re module for regex
from reportlab.pdfgen import canvas
from PyPDF2 import PdfMerger
from reportlab.lib.pagesizes import letter

# Initialize a blank PDF
def create_blank_pdf(output_path):
    c = canvas.Canvas(output_path)
    c.showPage()  # Add a blank page
    c.save()

# Function to append multiple files to a PDF
def append_pdfs(output_path, input_files):
    merger = PdfMerger()  # Create a PDF merger variable
    for file in input_files:
        merger.append(file)  # Append each file to the merger
    merger.write(output_path)  # Write the merged PDF to the output path
    merger.close()

# Function to convert a .jpeg file to a PDF
def convert_jpeg_to_pdf(jpeg_file, output_pdf):
    c = canvas.Canvas(output_pdf, pagesize=letter)
    c.drawImage(jpeg_file, 0, 0, width=letter[0], height=letter[1])  # Draw the image
    c.showPage()
    c.save()

# Example usage
if __name__ == "__main__":
    create_blank_pdf("blank.pdf")
    input_files = []  # List of files to append
    cwd = os.getcwd()  # Get the current working directory
    for file in os.listdir(cwd):  # Iterate through files in the directory
        if file.endswith(".jpeg"):  # Check for .jpeg files
            pdf_file = file.replace(".jpeg", ".pdf")  # Create a corresponding PDF filename
            convert_jpeg_to_pdf(file, pdf_file)  # Convert the .jpeg to a PDF
            input_files.append(pdf_file)  # Add the converted PDF to the input files list

    # Sort files based on the rightmost number in their names
    input_files.sort(key=lambda x: int(re.search(r'(\d+)(?!.*\d)', x).group(1)) if re.search(r'(\d+)(?!.*\d)', x) else 0)

    append_pdfs("merged.pdf", input_files)  # Merge the files
    print(input_files)  # Print the sorted list of appended files
