import os
import PyPDF2

project_path = os.getcwd()
directory_path = os.path.join(project_path, "17-PDFsAndSpreadsheetCSV", "02-PDFFiles")

wbp_path = os.path.join(directory_path, "Working_Business_Proposal.pdf")

def work_with_pdf(path, func):
    f = open(path, 'rb')
    pdf_reader = PyPDF2.PdfReader(f)

    func(pdf_reader)

    f.close()

def print_pages(pdf_reader):
    print(len(pdf_reader.pages))

def work_with_page_1(pdf_reader):
    page_one = pdf_reader.pages[0]

    page_one_text = page_one.extract_text()
    print(page_one_text)

def add_page(pdf_reader):
    page_one = pdf_reader.pages[0]

    pdf_writer = PyPDF2.PdfWriter()
    pdf_writer.add_page(page_one)

    write_to_pdf('Some_Brand_New_Doc.pdf', pdf_writer)

def write_to_pdf(name, pdf_writer):
    path = os.path.join(directory_path, name)
    
    pdf_output = open(path, 'wb')
    pdf_writer.write(pdf_output)

    pdf_output.close()

def print_all_pages(pdf_reader):
    pdf_text = []

    for i in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[i]
        text = page.extract_text()

        pdf_text.append(text)

    for pdf_text in pdf_text:
        print(pdf_text)
        

if __name__ == "__main__":
    # work_with_pdf(wbp_path, print_pages)
    
    # work_with_pdf(wbp_path, work_with_page_1)

    # work_with_pdf(wbp_path, add_page)

    work_with_pdf(wbp_path, print_all_pages)