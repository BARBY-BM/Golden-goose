import os
from datetime import datetime
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Authenticate
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

# Create Daily Folder
today = datetime.today().strftime('%Y-%m-%d')
folder_metadata = {'title': today, 'mimeType': 'application/vnd.google-apps.folder'}
folder = drive.CreateFile(folder_metadata)
folder.Upload()
folder_id = folder['id']

# Upload Reports
report_dir = os.path.expanduser("~/reports/")
for file_name in os.listdir(report_dir):
    file_path = os.path.join(report_dir, file_name)
    upload_file = drive.CreateFile({'title': file_name, 'parents': [{'id': folder_id}]})
    upload_file.SetContentFile(file_path)
    upload_file.Upload()
    print(f"Uploaded {file_name}")
