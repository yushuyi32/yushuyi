import pandas as pd


def my_read_excel(excel_path="D:\\VScode\\workhome\\test\\ykdtest\\data\\ykdtest.xlsx", skip_rows=1):
    try:
        # 读取 Excel 文件
        excelFile = pd.ExcelFile(excel_path)

        all_data = []  # 用来存储所有工作表的所有行数据

        for my_sheet_name in excelFile.sheet_names:
            # 读取每个工作表
            df = pd.read_excel(excelFile, sheet_name=my_sheet_name, skiprows=skip_rows)

            # 遍历每一行并保存
            for index, row in df.iterrows():
                all_data.append(row)
                print(row)  # 打印当前行数据

        return all_data  # 返回所有行的数据

    except Exception as e:
        print(f"读取 Excel 文件时出错: {e}")
        return None  # 如果出现错误，返回 None






# from unittest import result
# import pandas as pd
#
#
# def my_read_excel(excel_path="D:\\VScode\\workhome\\test\\ykdtest\\data\\ykdtest.xlsx", skip_rows=1):
#     excelFile = pd.ExcelFile(excel_path)
#     for my_sheet_name in excelFile.sheet_names:
#         df = pd.read_excel(excelFile, sheet_name=my_sheet_name)
#         for index, row in df.iterrows():
#             results = row
#             print(results)
#     return results

# def my_read_excel(excel_path="D:\\VScode\\workhome\\test\\ykdtest\\data\\ykdtest.xlsx",skip_first=True):
#     excelFile = pd.ExcelFile(excel_path)
#     for my_sheet_name in excelFile.sheet_names:
#         df = pd.read_excel(excelFile,sheet_name=my_sheet_name)
#         if skip_first == True:
#             start_row = 1
#         else:
#             start_row = 0
#         for index, row in df.iterrows():
#             results = row
#             print(results)
#     return results
