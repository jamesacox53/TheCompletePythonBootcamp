import os
import csv

project_path = os.getcwd()
directory_path = os.path.join(project_path, "17-PDFsAndSpreadsheetCSV", "01-CSVFiles")

example_path = os.path.join(directory_path, "example.csv")
makeup_new_path = os.path.join(directory_path, "makeup_new.csv")
to_save_file_path = os.path.join(directory_path, "to_save_file.csv")


def get_csv_data_lines(path):
    data = open(path, 'r', encoding="utf-8")

    csv_data = csv.reader(data)
    data_lines = list(csv_data)

    data.close()

    return data_lines

def print_data_lines(data_lines):
    for data_line in data_lines:
        print(data_line)

def get_all_emails(data_lines):
    all_emails = []

    for i in range(1, len(data_lines)):
        data_line = data_lines[i]
        
        email = data_line[3]
        all_emails.append(email)

    return all_emails

def get_all_full_names(data_lines):
    full_names = []

    for i in range(1, len(data_lines)):
        data_line = data_lines[i]
        
        first_name = data_line[1]
        last_name = data_line[2]
        full_name = first_name + " " + last_name

        full_names.append(full_name)

    return full_names

def write_csv_file(name, data_lines):
    file_path = os.path.join(directory_path, name)
    file_to_output = open(file_path, 'w', newline='')
    
    csv_writer = csv.writer(file_to_output, delimiter=",")
    csv_writer.writerows(data_lines)

    file_to_output.close()

if __name__ == "__main__":
    example_csv = get_csv_data_lines(example_path)
    # print_data_lines(example_csv)

    # print(example_csv[10])

    example_csv_emails = get_all_emails(example_csv)
    # print_data_lines(example_csv_emails)

    example_csv_full_names = get_all_full_names(example_csv)
    # print_data_lines(example_csv_full_names)

    write_csv_file("example2.csv", example_csv[0:10])