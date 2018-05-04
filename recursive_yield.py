# talkpython.fm
# find all the files in a given directory - drill down into all subfolders
# use recursive generator idea
import os


def get_files(path_to_folder):
    list_item = os.listdir(path_to_folder)

    for item in list_item:
        full_path = os.path.join(path_to_folder, item)

        if os.path.isfile(full_path):
            yield full_path

        elif os.path.isdir(full_path):
            # recursion
            get_files(full_path)


folder = 'D:\Git\ChangeManagementTool\ChangeManagementTool'
get_files(folder)
