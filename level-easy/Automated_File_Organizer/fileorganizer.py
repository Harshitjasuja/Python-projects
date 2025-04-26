# Automated File Organizer

# A Python script that automatically organizes files in a folder based on their extensions 
# (like .pdf, .jpg, .mp4, etc.). You can run it on your Downloads folder and it will clean it up.

import os
import shutil

# path to your folder you want to organize
folder_path = r"/Users/harshitjasuja/Desktop/college_work/python/projects/LEVEL-EASY"

# dictonary of folder names and file extensions
file_type = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Programs": [".exe", ".msi"],
    "Others": []
}

#create folder if not exist
for folder in file_type:
    folder_name = os.path.join(folder_path, folder)
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        
#move files to the respective folder
for filename in os.listdir(folder_path):
    file_ext = os.path.splitext(filename)[1].lower()
    file_moved = False
    
    for folder, extension in file_type.items():
        if file_ext in extension:
            src = os.path.join(folder_path, filename)
            dest = os.path.join(folder_path, folder, filename)
            shutil.move(src, dest)
            file_moved = True
            break
        
    # move unknown type to "others"
    if not file_moved and os.path.isfile(os.path.join(folder_path, filename)):
        shutil.move(os.path.join(folder_path, filename), os.path.join(folder_path, "others", filename))
        
print("files organized succesfully")