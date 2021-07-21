# coding:utf-8
from apscheduler.schedulers.blocking import BlockingScheduler
import zsy
def run():
    key=""
    zsy.main(key)

def appsch():
    scheduler = BlockingScheduler()
    #初始执行
    run()
    #开始调度
    #weeks days hours minutes
    scheduler.add_job(func=run,trigger='interval',hours=6)
    scheduler.start()

if __name__ == '__main__':
    appsch()


