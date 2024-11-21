import os
import time

def cleanup_old_files(directory, days):
  current_time = time.time()

  for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    if os.path.isfile(file_path):
      file_age = current_time - os.path.getmtime(file_path)
      if file_age > days * 86400:
        os.remove(file_path)
        print(f"Deleted {filename}")

cleanup_old_files("/home/ayroid/Downloads", 30)