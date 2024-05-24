import zipfile
import pathlib

def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, 'compressed.zip')
    with zipfile.ZipFile(dest_path , 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            filename = filepath.name
            archive.write(filepath, arcname=filename)

if __name__ == '__main__':
    make_archive(filepaths=['Bonus_16.py'], dest_dir='dest')