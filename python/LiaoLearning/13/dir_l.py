import os
import stat
import time
import argparse

def dir_l(path='.'):
    if not os.path.exists(path):
        raise FileNotFoundError(f"路径不存在：{path}")
    for filename in os.listdir(path):
        filepath = os.path.join(path,filename)
        file_stat = os.stat(filepath)
        # 文件类型和权限
        mode = file_stat.st_mode
        permissions = stat.filemode(mode)
        # 文件大小
        size = file_stat.st_size
        # 最后修改时间
        mtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(file_stat.st_mtime))

        print(f"{permissions}{size:10}{mtime} {filename}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="输出指定目录下所有文件和文件夹")
    parser.add_argument('path', help="想要输出目录下文件的路径")
    args = parser.parse_args()
    dir_l(args.path)