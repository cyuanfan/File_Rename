# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 14:54:32 2023

@author: s5011
"""

"""

import os

# 輸入要重命名的資料夾路徑
folder_path = input("請輸入要重命名的資料夾路徑：")

# 輸入檔名的前綴字串
prefix = input("請輸入檔名的前綴字串：")

# 取得資料夾中所有的檔案
files = os.listdir(folder_path)

# 取得檔案名稱中的數字，並依照數字大小排序
files_with_numbers = [(file_name, int("".join(filter(str.isdigit, os.path.splitext(file_name)[0])))) for file_name in files if "".join(filter(str.isdigit, os.path.splitext(file_name)[0]))]
files_with_numbers.sort(key=lambda x: x[1])

# 計算檔名中最大的數字的位數
max_num_digits = len(str(files_with_numbers[-1][1]))

# 重命名所有檔案
for i, (file_name, number) in enumerate(files_with_numbers):
    # 將數字轉換為補零後的字串
    num_str = str(number).zfill(max_num_digits)
    file_extension = os.path.splitext(file_name)[1]
    new_file_name = prefix + "_" + num_str + file_extension
    os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, new_file_name))

"""


import os
import re

# 指定要處理的資料夾路徑
folder_path = input("請輸入要重命名的資料夾路徑：")

# 取得資料夾中所有檔案的路徑列表
file_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# 排序檔案路徑列表，依據檔名中括弧內的數字大小或檔名最後面的數字大小來排序
def get_number_from_string(s):
    # 使用正規表達式找出字串中所有的數字
    numbers = re.findall(r'\d+', s)
    if len(numbers) == 0:
        return -1
    else:
        return int(numbers[-1])
sorted_file_paths = sorted(file_paths, key=lambda x: get_number_from_string(os.path.splitext(x)[0]))

# 讓使用者輸入檔名前綴字串
prefix = input("請輸入檔名前綴字串: ")


# 依序重新命名檔案
for i, f in enumerate(sorted_file_paths):
    # 取得檔案副檔名
    ext = os.path.splitext(f)[1]

    # 取得檔名中括弧內的數字，如果檔名中不含括弧，就取得檔名最後面的數字
    # zfill()設定補0的位數
    match = re.search(r'\[(\d+)\]', f)
    if match:
        number = int(match.group(1))
        new_file_name = f"{prefix}{str(number).zfill(3)}{ext}"
    else:
        number = i + 1
        new_file_name = f"{prefix}{str(number).zfill(3)}{ext}"

    # 重新命名檔案
    os.rename(f, os.path.join(folder_path, new_file_name))



"""
import os
import re

# 檔案所在的資料夾路徑
folder_path = input("請輸入檔案所在的資料夾路徑：")

# 檔名前綴字串
prefix = input("請輸入檔名前綴字串（按 Enter 跳過）：")

# 取得資料夾內所有檔案的列表
files = os.listdir(folder_path)

# 找到檔名中的數字，如果沒有括弧就找最後一個數字
pattern = r'\d+'
if any('(' in f and ')' in f for f in files):
    pattern = r'\(\d+\)'

# 將檔案名稱按照數字大小排序
files.sort(key=lambda x: int(re.findall(pattern, x)[-1]))

# 重新命名檔案
for i, file in enumerate(files):
    # 取得檔案的副檔名
    file_ext = os.path.splitext(file)[1]

    # 補足數字的前置0
    num_str = re.findall(pattern, file)[-1]
    num_str = num_str.zfill(3)

    # 新檔名
    new_file_name = prefix + num_str + file_ext

    # 舊檔案路徑
    old_file_path = os.path.join(folder_path, file)

    # 新檔案路徑
    new_file_path = os.path.join(folder_path, new_file_name)

    # 重新命名
    os.rename(old_file_path, new_file_path)
    print(f"{old_file_path} 已更名為 {new_file_path}")

"""