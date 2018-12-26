import sys
def application(environ,start_response):
    start_response('200 OK',[('Content-Type','text/html; charset=utf-8')])
    type = sys.getfilesystemencoding()
    print(type)
    strr = '<h1>你好 王根！</h1>'.encode()
    return [strr]