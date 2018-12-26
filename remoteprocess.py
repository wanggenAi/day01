import random,time
from multiprocessing.managers import BaseManager

#发送任务的队列
task_queue = queue.Queue()
#接收结果的队列
result_queue = queue.Queue()

#从basemanager继承的queuemanager
class QueueManger(BaseManager):
    pass
QueueManger.register('get_task_queue',callable=lambda: task_queue)
QueueManger.register('get_result_queue',callable=lambda: result_queue)
#绑定5000端口，设置验证码abc
manager = QueueManger(address=('',5000),authkey=b'abc')
#启动queue
manager.start()
task = manager.get_task_queue()
result = manager.get_result_queue()
#主服务端负责放多个任务进去
for i in range(10):
    n = random.randint(0,10000)
    print('在task任务中放进去了 %s ' % n)
    task.put(n)
print("等待其他服务器上传任务的计算结果...")
for i in range(10):
    r = result.get(timeout=10)
    print('任务的计算结果是： %s' % r)
#关闭
manager.shutdown()
print('master exit')