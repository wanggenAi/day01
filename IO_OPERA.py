import os
#print(os.environ.get('PATH'))
#print(os.path.abspath('.'))
import json
#print(json.dumps('中国',ensure_ascii=False))
print('Process (%s) start...' % os.getpid())
pid = os.fork()
if pid == 0:
    print('我是子进程 %s ,父进程是 %s' % (os.getpid(),os.getppid()))
else:
    print('我是父进程 %s ,子进程是 %s' % (os.getpid(),pid))；；；

