import shutil

COPY_FILES = [
    ('.env.example', '.env')
]

for origin, dest in COPY_FILES:
    print(f'Copying {origin} to {dest}')
    shutil.copyfile(origin, dest)
