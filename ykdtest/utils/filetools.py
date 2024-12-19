# 1.保存信息到文件
import os


def save_file(file_path="D:/VScode/workhome/test/ykdtest/conf/token.txt", token=''):
    try:
        # (file_path=然认/conf/token.txt,token=默认为空
        # 到文件中以写入的模式把token写入token.txt 中
        dir_name = os.path.dirname(file_path)
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
        with open(file_path, "w", encoding='utf-8') as f:  # 新建一个文件保存在 conf 中
            f.write(token + "\n")
            print(f"Token已成功保存到{file_path}")
    except Exception as e:
        print(f"保存文件时出错：{e}")


# 2.读取txt 文件
# 读取 token 文件
def read_file(file_path="./conf/token.txt"):
    try:
        with open(file_path, "r") as f:
            token = f.read().strip()  # 使用 strip() 去掉前后的空白字符（如换行符）
            return token
    except FileNotFoundError:
        print(f"文件 {file_path} 不存在")
        return None  # 或者返回一个空字符串 ""
    except Exception as e:
        print(f"读取文件时出错: {e}")
        return None  # 或者返回一个空字符串 ""
# def read_file(file_path="./conf/token.txt"):
#     with open(file_path,"r")as f: #r表示只读模式
#         token =f.read()
#         return token # 返回数据
