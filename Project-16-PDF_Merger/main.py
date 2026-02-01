import os 
from pypdf import PdfWriter
file_path = input("Enter path of file : ").strip('"')
file_name = input("Enter the name for the new file: ")
if not file_name.endswith(".pdf"):
    file_name = file_name + ".pdf"
list_folder = os.listdir(file_path)
list_folder.sort()
merger = PdfWriter()
for file in list_folder:
    if file == file_name :
        continue
    if file.lower().endswith(".pdf"):
        try:
            general_path = os.path.join(file_path,file)
            merger.append(general_path)
            print(f"Adding file {file} ")
        except Exception as e:
            print("Wrong file skipping..")
merger.write(os.path.join(file_path,file_name ))
merger.close()
print("Everything is OK")


