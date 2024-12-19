import pytest
import requests
import os
import sys
import json
import ast
from utils.filetools import save_file
from utils.exceltools import my_read_excel


def test_01_login_success():
    # 读取Excel中的登录数据
    data_res = my_read_excel("D:/VScode/workhome/test/ykdtest/data/ykdtest.xlsx", "login")
    url = data_res[0][2]  # 获取URL
    headers = ast.literal_eval(data_res[0][4])  # 安全解析请求头
    data = ast.literal_eval(data_res[0][5])  # 安全解析请求参数

    try:
        # 发送POST请求
        response = requests.post(url, headers=headers, json=data)

        # 检查响应状态码
        if response.status_code == 200:
            jsondata = response.json()
            token = jsondata.get('result', {}).get('token')

            if token:
                print("登录成功，token：", token)
                save_file(token=token)  # 保存token
                return token
            else:
                print("登录失败：未获取到token")
                return "登录失败：未获取到token"
        else:
            print(f"登录失败: HTTP 状态码 {response.status_code}")
            return f"登录失败: HTTP 状态码 {response.status_code}"

    except requests.exceptions.RequestException as e:
        print(f"请求失败：{e}")
        return f"请求失败：{e}"


if __name__ == '__main__':
    test_01_login_success()
# import pytest
# import requests
# import os
# import sys
# import json
# from utils.filetools import save_file
# from utils.exceltools import my_read_excel
#
#
# def test_01_login_success():
#     data_res = my_read_excel("D:/VScode/workhome/test/ykdtest/data/ykdtest.xlsx", "login")
#     url = data_res[0][2]
#     headers = eval(data_res[0][4])
#     data = eval(data_res[0][5])
#     try:
#         response = requests.post(url, headers=headers, json=data)
#         if response.status_code != 0:
#             jsondata = response.json()
#             token = jsondata['result'].get('token')
#             if token:
#                 print("登录成功，token：", token)
#                 save_file(token=token)
#                 return token
#             else:
#                 print("登陆失败：未获取到token")
#                 return "登陆失败：未获取到token"
#         else:
#             print(f"登录失败:业务状态码{response.status_code}")
#             return f"登录失败:业务状态码{response.status_code}"
#     except requests.exceptions.RequestException as e:
#         print(f"请求失败：{e}")
#         return f"请求失败：{e}"
