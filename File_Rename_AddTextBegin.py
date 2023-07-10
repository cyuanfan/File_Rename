# 將資料夾內的所有檔案名添加指定的前綴字串

import os

def add_prefix_to_files(folder_path, prefix):
    """
    Add a prefix string to all files in the specified folder path.

    Args:
        folder_path (str): The path to the folder containing the files to rename.
        prefix (str): The prefix string to add to the file names.
    """
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            new_filename = prefix + filename
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))

folder_path = 'C:/other/test'
prefix = 'Img_'
add_prefix_to_files(folder_path, prefix)
