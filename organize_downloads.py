import os
import shutil

downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
print("Looking in:", downloads_folder)

file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt'],
    'Archives': ['.zip', '.rar', '.7z'],
    'Videos': ['.mp4', '.mkv'],
    'Music': ['.mp3', '.wav']
}

for filename in os.listdir(downloads_folder):
    file_path = os.path.join(downloads_folder, filename)
    print("Found:", filename)

    if os.path.isfile(file_path):
        file_ext = os.path.splitext(filename)[1].lower()

        moved = False
        for folder_name, extensions in file_types.items():
            if file_ext in extensions:
                folder_path = os.path.join(downloads_folder, folder_name)
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                shutil.move(file_path, os.path.join(folder_path, filename))
                print(f"Moved {filename} to {folder_name}")
                moved = True
                break

        if not moved:
            print(f"No matching category for {filename}")
