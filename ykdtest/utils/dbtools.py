import pymysql #要想用pymysqL
lef query(sql)：
    # 固定的方法
    db = pymysql.connect(host='47.94.108.52',user='wuyulin',password="jU3s50E5"db='')
# host 是要连接的数据库的IP 地址
# user 数据库账号 password 密码 db 表示要打开的数据库名字
# 获取查询窗口：游标
    cur = db.cursor()
# 执行sql语句
    cur.execute(sql)
# 获取所有的结果
    res = cur.fetchall()
# 关闭数据库连接
    db.close()
# 返回结果
    return res
if _name_ =="_main_":
    a = query("select * from t_user where id = '我是id'") 
    #引号原则：外双内单/内单外双，内外引号不同即可
    print(a)