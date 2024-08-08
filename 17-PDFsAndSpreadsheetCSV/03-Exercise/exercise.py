import os
import csv
import PyPDF2
import re

project_path = os.getcwd()
directory_path = os.path.join(project_path, "17-PDFsAndSpreadsheetCSV", "03-Exercise")

# Task One
def task_one():
    link_path = os.path.join(directory_path, "find_the_link.csv")
    link_data_lines = get_csv_data_lines(link_path)
    
    link_str = get_link_str(link_data_lines)
    print(link_str)

def get_csv_data_lines(path):
    data = open(path, 'r', encoding="utf-8")

    csv_data = csv.reader(data)
    data_lines = list(csv_data)

    data.close()

    return data_lines

def get_link_str(data_lines):
    link_str = ""
    
    for i in range(len(data_lines)):
        data_line = data_lines[i]

        link_part = data_line[i]
        link_str += link_part

    return link_str


# Task 2
def task_two():
    pdf_path = os.path.join(directory_path, "Find_the_Phone_Number.pdf")

    work_with_pdf(pdf_path, find_phone_num_in_pdf)

def work_with_pdf(path, func):
    f = open(path, 'rb')
    pdf_reader = PyPDF2.PdfReader(f)

    func(pdf_reader)

    f.close()

def find_phone_num_in_pdf(pdf_reader):
    text_list = get_all_text_from_pdf(pdf_reader)
    phone_nums = []

    phone_pattern = r"\d{3}.\d{3}.\d{4}"
    
    for text in text_list:
        matches = re.findall(phone_pattern, text)

        phone_nums.extend(matches)
    
    print(phone_nums)

def get_all_text_from_pdf(pdf_reader):
    text_list = []

    for page in pdf_reader.pages:
        text = page.extract_text()

        text_list.append(text)

    return text_list


if __name__ == "__main__":
    task_one()

    task_two()