import time, sys, queue
from multiprocessing.managers import BaseManager
# 创建类似的QueueManager:
class QueueManager(BaseManager):
    pass
QueueManager.register("get_task_queue")
QueueManager.register("get_result_queue")

server_addr = '192.168.208.131'
print('连接master服务器:%s' % server_addr)
m = QueueManager(address=(server_addr,5000),authkey=b'abc')
m.connect()
task = m.get_task_queue()
result = m.get_result_queue()
for i in range(10):
    try:
        n = task.get(timeout=10)
        print('获取到了任务数据：%s' % n)
        r = '%d * %d = %d' % (n, n, n * n)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print('task is empty')

print('worker exit')