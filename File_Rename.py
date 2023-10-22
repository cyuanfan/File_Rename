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

# 讓使用者決定檔名的數字編號是否加上括弧
bracket = input("是否將數字放入括弧內: y/n ?")
if bracket == 'y':
    add_bracket = True
else:
    add_bracket = False


# 依序重新命名檔案
for i, f in enumerate(sorted_file_paths):
    # 取得檔案副檔名
    ext = os.path.splitext(f)[1]

    # 取得檔名中括弧內的數字，如果檔名中不含括弧，就取得檔名最後面的數字
    # zfill()設定補0的位數
    match = re.search(r'\[(\d+)\]', f)
    if match:
        number = int(match.group(1))
    else:
        number = i + 1

    if add_bracket == True:
        str_number = '(' + str(number).zfill(3) + ')'
    else:
        str_number = str(number).zfill(3)

    new_file_name = f"{prefix}{str_number}{ext}"

    # 重新命名檔案
    os.rename(f, os.path.join(folder_path, new_file_name))

