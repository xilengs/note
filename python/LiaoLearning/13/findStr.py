import os
import sys
import argparse

def findStr(path='.', s='.py'):
    if not os.path.exists(path):
        raise FileNotFoundError(f"路径不存在：{path}")
    for filename in os.listdir(path):
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
            findStr(filepath,s)
        else:
            if s in filename:
                print(f"{filepath}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="查找目录以及子目录下包含指定字符串的文件")
    parser.add_argument('path', help="要查找的目录")
    parser.add_argument('s', help='要查找的字符串')
    args = parser.parse_args()

    findStr(args.path, args.s)
    
#    if len(sys.argv) < 3:
#        print(f"用法: python {sys.argv[0]} <目录><要查找的字符串>")
#    else:
#        path = sys.argv[1]
#        s = sys.argv[2]
#        findStr(path, s)