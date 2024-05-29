import zipfile

def extract_archive(archivepath, dest_dir):
    with zipfile.ZipFile(archivepath, 'r') as archive:
        archive.extractall(dest_dir)


if __name__ == '__main__':
    extract_archive(r'C:\Users\tokarski-to\Pycharm codes\Course\Bonus\compressed.zip',
                    dest_dir=r"C:\Users\tokarski-to\Pycharm codes\Course\Bonus\files")