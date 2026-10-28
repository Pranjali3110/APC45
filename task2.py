import os
import shutil

#path of your folder here
folder = r"C:\Users\HP\Desktop\APC LAB\task2"

# File categories
categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt"],
    "Excel": [".xls", ".xlsx", ".csv"],
    "PowerPoint": [".ppt", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Python": [".py"],
    "Java": [".java"],
    "C_Cpp": [".c", ".cpp", ".h"],
    "Archives": [".zip", ".rar", ".7z"],
}


for file in os.listdir(folder):

    file_path = os.path.join(folder, file)

    # Ignore folders
    if os.path.isdir(file_path):
        continue

    # Get file extension
    extension = os.path.splitext(file)[1].lower()

    found = False

    # Find category
    for category, extensions in categories.items():

        if extension in extensions:

            category_folder = os.path.join(folder, category)

            # Create category folder if it doesn't exist
            if not os.path.exists(category_folder):
                os.mkdir(category_folder)

            # Move file
            shutil.move(file_path, os.path.join(category_folder, file))

            print(file, "->", category)

            found = True
            break

    # Files with unknown extensions
    if not found:

        other_folder = os.path.join(folder, "Others")

        if not os.path.exists(other_folder):
            os.mkdir(other_folder)

        shutil.move(file_path, os.path.join(other_folder, file))

        print(file, "-> Others")


print("\nAll files have been organized successfully!")