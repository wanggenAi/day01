def printI():
    n = 'heihei'
    for i in range(100000):
        n = yield i
        print(n)
tt = printI()
print(tt.send(None))
print(tt.send('aa'))
print(tt.send('bb'));;