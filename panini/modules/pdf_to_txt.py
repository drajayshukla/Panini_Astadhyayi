import os
from PyPDF2 import PdfReader


def convert_pdfs_to_text(input_path):
    # Normalize the path
    input_path = os.path.expanduser(input_path)

    # Check if the path is valid
    if not os.path.exists(input_path):
        print(f"Invalid path: {input_path}")
        return

    # If it's a directory, process all PDFs in it
    if os.path.isdir(input_path):
        for file_name in os.listdir(input_path):
            if file_name.endswith(".pdf"):
                pdf_path = os.path.join(input_path, file_name)
                process_pdf(pdf_path)
    else:
        print(f"The provided path is not a directory: {input_path}")


def process_pdf(pdf_path):
    try:
        # Extract text from the PDF
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()

        # Save the text to a file with "_mba.txt" suffix
        base_name = os.path.splitext(os.path.basename(pdf_path))[0]
        output_file = f"{base_name}_mba.txt"
        with open(output_file, "w", encoding="utf-8") as txt_file:
            txt_file.write(text)

        print(f"Converted: {pdf_path} -> {output_file}")
    except Exception as e:
        print(f"Failed to process {pdf_path}: {e}")


# Input path (folder or file)
input_path = input("Enter the folder path containing PDF files: ").strip().strip("'").strip('"')
convert_pdfs_to_text(input_path)
