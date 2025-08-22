# argparse
# 在命令行，经常需要获取命令行的参数。python内置的sys.argv保存了完整的参数列表，可以从中解析出需要的参数
# python copy.py source copy
# 这种方式可以应付简单的参数，但参数稍微复杂点，解析起来就非常麻烦了
# 为了简化参数解析，可以使用内置的argparse库，定义好各个参数类型后，它能直接返回有效的参数


# 现在定义一个备份MySQL数据库的命令行程序：
# host: 表示MySQL主机名或IP，不输入则默认为localhost
# port: 表示MySQL的端口号，int类型，不输入则默认为3306
# user: 表示登录MySQL的用户名，必须输入
# password: 表示登录MySQL的口令，必须输入
# gz: 表示是否压缩备份文件，不输入则默认为False
# outfile: 表示备份文件保存在哪，必须输入
# backup.py