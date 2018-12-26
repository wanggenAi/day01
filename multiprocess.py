from multiprocessing import Pool
import os,time,random

def long_time_task(name):
    print('Run task %s (%s)...' % (name,os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print('任务 %s 用时: %0.2f' % (name,(end-start)))


if __name__== '__main__':
    print('主进程（%s）开始运行' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task,args=(i,))
    print("等待所有进程都运行完成......")
    p.close()
    p.join()
    print("所有子进程运行结束");