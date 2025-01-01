import os
import shutil


def move_files_by_type(source_folder, destination_folder, file_extension):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    for filename in os.listdir(source_folder):
        if filename.endswith(file_extension):
            source_path = os.path.join(source_folder, filename)
            destination_path = os.path.join(destination_folder, filename)
            if os.path.exists(destination_path):
                os.remove(destination_path)
            shutil.move(source_path, destination_folder)
            print(f"Moved {filename} to {destination_folder}")


move_files_by_type("/home/ayroid/Downloads", "/home/ayroid/Downloads/pdfs", ".pdf")
move_files_by_type("/home/ayroid/Downloads", "/home/ayroid/Downloads/images", ".jpg")
move_files_by_type("/home/ayroid/Downloads", "/home/ayroid/Downloads/images", ".png")
move_files_by_type("/home/ayroid/Downloads", "/home/ayroid/Downloads/images", ".jpeg")
move_files_by_type("/home/ayroid/Downloads", "/home/ayroid/Downloads/zips", ".zip")
move_files_by_type("/home/ayroid/Downloads", "/home/ayroid/Downloads/videos", ".mp4")
move_files_by_type("/home/ayroid/Downloads", "/home/ayroid/Downloads/json", ".json")
move_files_by_type("/home/ayroid/Downloads", "/home/ayroid/Downloads/excels", ".xlsx")
move_files_by_type("/home/ayroid/Downloads", "/home/ayroid/Downloads/svgs", ".svg")
move_files_by_type("/home/ayroid/Downloads", "/home/ayroid/Downloads/docx", ".docx")
