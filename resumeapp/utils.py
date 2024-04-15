import re
import os
import zipfile
import textract
import xlsxwriter

def extract_resume_data(zip_file_path):
    extracted_data = []

    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        for filename in zip_ref.namelist():
            with zip_ref.open(filename) as file:
                text = extract_text_from_file(file)
                email = extract_email(text)
                contact_number = extract_contact_number(text)
                extracted_data.append({'Email': email, 'Contact Number': contact_number, 'Text': text})

    return extracted_data

def extract_text_from_file(file):
    # Extract text content from various file types
    content = ''
    filename, file_extension = os.path.splitext(file.name)

    if file_extension.lower() == '.pdf':
        content = textract.process(file)
    elif file_extension.lower() == '.docx':
        content = textract.process(file)
    elif file_extension.lower() == '.txt':
        content = file.read().decode('utf-8')

    return content

def extract_email(text):
    # Extract email address using regular expression
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_regex, text)
    return emails[0] if emails else ''

def extract_contact_number(text):
    # Extract contact number using regular expression
    phone_regex = r'\b(?:\+?(\d{1,3}))?[-. (]*?(\d{3})[-. )]*?(\d{3})[-. ]*(\d{4})\b'
    phone_numbers = re.findall(phone_regex, text)
    formatted_numbers = []
    for match in phone_numbers:
        formatted_numbers.append('-'.join(match))
    return ', '.join(formatted_numbers)

def generate_excel_report(extracted_data, output_path):
    workbook = xlsxwriter.Workbook(output_path)
    worksheet = workbook.add_worksheet()

    # Write headers
    headers = ['Email', 'Contact Number', 'Text']
    for col, header in enumerate(headers):
        worksheet.write(0, col, header)

    # Write data
    for row, data in enumerate(extracted_data, start=1):
        worksheet.write(row, 0, data.get('Email', ''))
        worksheet.write(row, 1, data.get('Contact Number', ''))
        worksheet.write(row, 2, data.get('Text', ''))

    workbook.close()

    return output_path
