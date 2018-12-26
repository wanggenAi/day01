from wsgiref.simple_server import make_server

from webtest import application

httpd = make_server('',8000,application)
print('开始监听8000....')
httpd.serve_forever()
