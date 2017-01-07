import os
import re

folder = os.getcwd() + os.path.sep + 'files'
prefix = re.compile('^\d+')


def rename_file(filename):
    print(filename)


def rename_files():
    files = os.listdir(folder)

    for filename in files:
        # os.chdir has side effect

        try:
            old_name = folder + os.path.sep + filename
            new_name = folder + os.path.sep + prefix.sub('', filename)
            os.rename(old_name, new_name)
        except FileNotFoundError:
            print('error')


rename_files()
