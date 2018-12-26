class ClassA(object):
    def __init__(self,classname):
        self.classname = classname
    def __getattr__(self, attr):
        return('invoke __getattr__', attr)

class Chain(object):
    def __init__(self,path=''):
        self._path = path
    def __getattr__(self, attr):
        return Chain('%s/%s' % (self._path ,attr))
    def __str__(self):
        return self._path

    __repr__ = __str__

class GitHub(object):
    def __init__(self,path = ''):
        self._path = path
    def __getattr__(self, attr):
        return GitHub('%s/%s' % (self._path,attr) )
    def user(self,uname):
        return GitHub('%s/:%s' % (self._path,uname))
    def __str__(self):
        return self._path
    __repr__ = __str__

#print(GitHub().users.user("michale").repos)

from enum import Enum, unique
Month = Enum('Month',('Jan','Fab', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
'''for name,member in Month.__members__.items():
    print(name,"=>",member,',',member.value)'''

@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

#print(Weekday.Mon.value)
class ListMetaclass(type):
    def __new__(cls,name,bases,attrs):
        attrs['add'] = lambda self,value: self.append(value)
        return type.__new__(cls,name,bases,attrs)

class MyList(list,metaclass=ListMetaclass):
    pass

L = MyList()
L.add(1)
#print(L)

class Field(object):

    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

class StringField(Field):

    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):

    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')

class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
            attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        attrs['__table__'] = name # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)

class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

#u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd',yaya='danei')
#print(u.__getattr__("yaya"))
#u.save()


