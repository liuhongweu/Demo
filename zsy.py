from getAllPages import getAllPages
from getAllurl import getAllUrls
from tools import *
from writeToDB import write

def main(key):

    urls = getAllUrls(key)
    if urls:
        getAllPages(key)
        write(key)
    else:
        printTip("未查到相关数据")


if __name__ == '__main__':
    main("")
