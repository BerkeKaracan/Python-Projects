import os
import shutil
import time
print("--SMART FILE ORGANIZER--")
target_dir = input("Please paste the folder path to organize : ").strip('"')
if not os.path.exists(target_dir):
    print(" ERROR : The specified folder does not exist! ")
    exit()
extensions = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Musics":    [".mp3", ".wav", ".flac"],
    "Programs": [".exe", ".msi", ".bat", ".sh"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"]
}
print(f" Scanning :  {target_dir} ...")
all_files = os.listdir(target_dir)
moved_count = 0
for file_name in all_files:
    source_path =os.path.join(target_dir, file_name)
    if os.path.isdir(source_path):
        continue
    file_extension = os.path.splitext(file_name)[1].lower()
    moved = False
    for folder_name, ext_list in extensions.items():
        time.sleep(0.5)
        if file_extension in ext_list:
            target_folder = os.path.join(target_dir, folder_name)
            if not os.path.exists(target_folder):
                os.makedirs(target_folder)
                print(f"Created folder : '{target_folder}'")
            destination_path = os.path.join(target_folder, file_name)
            try:
                shutil.move(source_path, destination_path)
                print(f"Moving : '{file_name} -> {folder_name}'")
                moved_count +=1
                moved = True
            except Exception as e:
                print(f"Error  {file_name} : {e}")
            break
print(f" Organization Complete ! {moved_count} files moved.")
input("Press ENTER to exit...")
