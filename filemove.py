import os
import shutil
from pathlib import Path

def filemove(file_groups):
    source = Path('C:\\Users\\phalm\\Downloads')
    for folder, extensions in file_groups.items():
        dest = source / folder
        dest.mkdir(exist_ok=True)
        for ext in extensions:
            files = source.glob(f'*.{ext}')
            for file in files:
                dest_file = dest / file.name
                if dest_file.exists():
                    print(f'Skipping {file}, file already exists in {dest}')
                else:
                    print(f'Moving {file} to {dest}')
                    shutil.move(str(file), str(dest_file))

file_groups = {
    'Images': ['png', 'jpg', 'jpeg', 'heic'],
    'Music': ['mp3', 'wav'],
    'Videos': ['mp4'],
    'Archives': ['rar', 'zip'],
    'Documents': ['pdf', 'doc', 'docx', 'ppt', 'pptx', 'xls', 'xlsx', 'csv', 'txt']
}

filemove(file_groups)