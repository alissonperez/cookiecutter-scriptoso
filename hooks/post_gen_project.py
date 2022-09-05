import os
import shutil

COPY_FILES = [
    ('.env.example', '.env')
]

for origin, dest in COPY_FILES:
    print(f'Copying {origin} to {dest}')
    shutil.copyfile(origin, dest)


remove_files = []


if '{{ cookiecutter.kafka }}'.lower().strip() != 'y':
    remove_files.append('kafkautil.py')


for path in remove_files:
    path = path.strip()
    if path and os.path.exists(path):
        if os.path.isdir(path):
            os.rmdir(path)
        else:
            os.unlink(path)
