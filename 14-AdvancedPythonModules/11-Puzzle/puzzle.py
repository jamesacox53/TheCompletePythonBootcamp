import os
import zipfile
import re

def unzip_puzzle(directory_path):
    zip_file_path = os.path.join(directory_path, 'unzip_me_for_instructions.zip')
    zip_extract_path = os.path.join(directory_path, 'unzipped_files')
    
    zip_obj = zipfile.ZipFile(zip_file_path, 'r')
    zip_obj.extractall(zip_extract_path)

def do_puzzle(directory_path):
    puzzle_path = os.path.join(directory_path, "unzipped_files", "extracted_content")

    phone_nums = find_phone_numbers(puzzle_path)
    print(phone_nums)

def find_phone_numbers(puzzle_path):
    phone_nums = []
    
    for (dirpath, dirnames, filenames) in os.walk(puzzle_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)

            f = open(file_path, 'r')
            file_content = f.read()
            
            search_file(file_content, phone_nums)
            
            f.close()

    return phone_nums

def search_file(file_content, phone_nums):
    phone_pattern = r"\d{3}-\d{3}-\d{4}"

    matches = re.findall(phone_pattern, file_content)
    for match in matches:
        phone_nums.append(match)

if __name__ == '__main__':
    directory_path = os.path.join(os.getcwd(), "14-AdvancedPythonModules", "11-Puzzle")
    
    unzip_puzzle(directory_path)
    do_puzzle(directory_path)