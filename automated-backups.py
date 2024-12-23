import shutil
import os
from datetime import datetime
import zipfile


def backup_and_zip_files(source_folder, backup_folder):
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)

    timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    backup_zip_filename = os.path.join(backup_folder, f"backup-{timestamp}.zip")

    with zipfile.ZipFile(backup_zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(source_folder):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, source_folder))

    print(f"Backup created at {backup_zip_filename}")


backup_and_zip_files("/home/ayroid/Downloads/images", "/home/ayroid/Documents/Backups")

# To Automate these tasks use CRON jobs -

# Open Crontab file: crontab -e
# Add the following line to run the script every day at 12:00 PM: 0 12 * * * python3 /home/ayroid/Documents/Private/DevOps/automated-backups.py
# Save and exit the crontab file. The script will now run every day at 12:00 PM.