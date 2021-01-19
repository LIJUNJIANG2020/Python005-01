# 以下代码使用 shift + enter 执行
# 类方法相关操作

# 普通方法
import re


class Person:
    def normal_func():
        print('普通的函数')

    def method(self):
        print('方法')


Person.normal_func()  # 普通的函数
Person().normal_func
# <bound method Person.normal_func of <__main__.Person object at 0x7fe68f163890>>
Person().normal_func()
# TypeError: normal_func() takes 0 positional arguments but 1 was given
sorted(Person.__dict__.items())
# [('__dict__', <attribute '__dict__' of 'Person' objects>), ('__doc__', None),
# ('__module__', '__main__'), ('__weakref__', <attribute '__weakref__' of 'Person' objects>),
# ('method', <function Person.method at 0x7fe68f15def0>),
# ('normal_func', <function Person.normal_func at 0x7fe68f15de60>)]


Person.method()
# TypeError: method() missing 1 required positional argument: 'self'
Person.method(Person())   # 方法
Person().method
# <bound method Person.method of <__main__.Person object at 0x7fe68f163c50>>
Person().method()   # 方法

# 类方法
class Person:
    @classmethod
    def class_method(cls):
        print('类方法')
        print(f'{cls}`s name {cls.__name__} ')
        cls.HEIGHT = 170


Person.class_method  # <bound method Person.class_method of <class '__main__.Person'>>
Person.class_method()
# 类方法
# <class '__main__.Person' >`s name Person
tom = Person()
tom.class_method    # <bound method Person.class_method of <class '__main__.Person'>>
tom.class_method()
# 类方法
# <class '__main__.Person' >`s name Person
Person.__dict__
# mappingproxy({'__module__': '__main__',
# 'class_method': < classmethod object at 0x7fe68f163c10 > ,
# '__dict__': < attribute '__dict__' of 'Person' objects > ,
# '__weakref__': < attribute '__weakref__' of 'Person' objects > ,
# '__doc__': None, 'HEIGHT': 170})
tom.__dict__
# {}

# 静态方法
class Person:
    HEIGHT = 170

    @staticmethod
    def static_method():
        print('静态方法')
        print(Person.HEIGHT)


Person.static_method  # <function Person.static_method at 0x7fe68f169170>
Person.static_method()
# 静态方法
# 170
Person().static_method  # <function Person.static_method at 0x7fe68f169170>
Person().static_method()
# 静态方法
# 170
Person.__dict__
# mappingproxy({'__module__': '__main__',
# 'HEIGHT': 170,
# 'static_method': < staticmethod object at 0x7fe68f1639d0 > ,
# '__dict__': < attribute '__dict__' of 'Person' objects > ,
# '__weakref__': < attribute '__weakref__' of 'Person' objects > ,
# '__doc__': None})

# 实战

class Person:
    def method(self):
        print(f'{self}`s method')


tom = Person()
tom.method()  # <__main__.Person object at 0x7fe68f163ed0>`s method
Person.method()  # TypeError: method() missing 1 required positional argument: 'self'
Person.method(tom)  # <__main__.Person object at 0x7fe68f163ed0>`s method
# <__main__.Person object at 0x7fe68f163ed0>`s method
tom.__class__.method(tom)


# 其它示例
# 示例-1 让实例的方法成为类方法
class Kls1():
    bar = 1

    def foo(self):
        print('in foo')

    @classmethod
    def class_foo(cls):
        print(cls.bar)
        print(cls.__name__)
        cls().foo()  # 调用实例方法


Kls1.class_foo()
'''
1
Kls1
in foo
'''
##########################
# 示例-2


class Kls2():
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def print_name(self):
        print(f"first name is {self.fname}")
        print(f"last name is {self.lname}")


me = Kls2('junjiang', 'Li')
me.print_name()

# 需求： 需要接收 junjiang-li的输入
# 方法一: 增加预处理函数


def pre_name(obj, name):
    fname, lname = name.split('-')
    return obj(fname, lname)


me = pre_name(Kls2, "junjiang-Li")
me.print_name()

# 方法2： 使用类方法


import re
import sys
class Kls3():
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    @classmethod
    def pre_name(cls, name):
        try:
            spl = re.search(r'\W', name).group()
        except:
            try:
                spl = re.search(r'_', name).group()
            except:
                print('err')
                sys.exit(1)
        # print(spl)
        fname, lname = name.split(spl)
        return cls(fname, lname)

    def print_name(self):
        print(f"first name is {self.fname}")
        print(f"last name is {self.lname}")



me = Kls3.pre_name('junjiang_li')
me.print_name()
you = Kls3('si', 'Li')
you.print_name()
###########################
# 示例- 3
class Frult(object):
    total = 0

    @classmethod
    def print_total(cls):
        print(cls.total)
        print(id(Frult.total))
        print(id(cls.total))

    @classmethod
    def set(cls, value):
        print(f'calling {cls}, {value}')
        cls.total = value

class Apple(Frult):
    pass

class Orange(Frult):
    pass


Apple.set(100)  # calling <class '__main__.Apple'>, 100
Apple.print_total()
# 100
# 4540134032
# 4540137232

Orange.set(200)  # calling <class '__main__.Orange'>, 200
Orange.print_total()
# 200
# 4540134032
# 4540140432


org = Orange()
org.set(300)  # calling <class '__main__.Orange'>, 300
Orange.print_total()
# 300
# 4540134032
# 140323017847472

# 静态方法
# 示例-1
import datetime
class Story(object):
    snake = 'Python'
    def __init__(self, name):
        self.name = name

    @staticmethod
    def god_come_go():
        if datetime.datetime.now().month % 2:
            print('god is coming')

Story.god_come_go()
Story('athor').god_come_go()


# 属性描述器
# __getattribute__()
# 访问一个不存在属性时：
class Human():
    def __init__(self, name):
        self.name = name

h1 = Human('Adam')
h2 = Human('Eve')

h1.name = "Python"
h1.name

del h1.name
h1.name  # AttributeError: 'Human' object has no attribute 'name'

# 对比1
class Human2():
    def __init__(self):
        self.age = 10
    
    # 显示的实现 __getattribute__() 
    def __getattribute__(self, item):
        print(f'__getattribute__ called item:{item}')


h1 = Human2()
h1.age      # __getattribute__ called item:age
h1.noattr   # __getattribute__ called item:noattr

'''
结论：
当一个实例去获取属性时，无论该属性是否存在，系统底层都会去调用__getattribute__()方法，
截获并改变这一行为的结果
'''
# 对比2： 
class Human3(object):
    def __init__(self):
        self.age = 10
    
    # 对正常的实例获取属性进行拦截，增加一个hook操作
    def __getattribute__(self, item):
        print(f'__getattribute__ called item:{item}') # 增加自已的操作
        return super().__getattribute__(item)  # 调用父类的__getattribute__()

h1 = Human3()
h1.age
# __getattribute__ called item: age
# 10
h1.noattr 
# __getattribute__ called item: noattr
# Traceback(most recent call last):
#   File "<stdin>", line 1, in <module >
#   File "<stdin>", line 6, in __getattribute__
# AttributeError: 'Human3' object has no attribute 'noattr'

# 对比3 ：
class Human4(object):
    def __getattribute__(self, item):
        # 将不存在的属性的值设置为100并返回，
        print(f'Human2:__getattribute__({item})')
        try:
            return super().__getattribute__(item)
        except Exception as e:
            self.__dict__[item] = 100
            return 100

h1 = Human4()
print(h1.noattr)
# Human2: __getattribute__(noattr)
# Human2: __getattribute__(__dict__)  # self.__dict__[item] = 100 也调用了__getattribute__() __dict__ 也是实例的属性
# 100

##########################################
## __getattr__()  仅对未定义的属性进行拦截

class Human(object):
    def __init__(self):
        self.age = 18

    def __getattr__(self, item):
        print(f'__getattr__ called item: {item}')
        return "Ok"

h1 = Human()
# 存在属性，未调用 __getattr__()
h1.age   # 18

# 不存在属性，调用了 __getattr__()
h1.noattr
# __getattr__ called item: noattr
# 'Ok'

# 应用示例 - 1：
class Human1(object):
    def __init__(self):
        self.age = 18

    def __getattr__(self, item):
        # 对指定属性做处理：fly 返回 superman, 其它属性返回None
        self.item = item
        if self.item == 'fly':
            return 'superman'

h1 = Human1()
h1.age # 18
h1.fly  # 'superman'
print(h1.noattr)  # None

## 同是定义__getattr__() 和 __getattribute__()时
class Human(object):
    def __init__(self):
        self.age = 18

    def __getattr__(self, item):
        print(f"__getattr__ called item: {item}")
        return "Err 404, 你请求的参数不存在"

    def __getattribute__(self, item):
        print(f"__getattribute__ called item: {item}")
        return super().__getattribute__(item)

h1 = Human()
h1.age
# __getattribute__ called item: age
# 18
h1.noattr
# __getattribute__ called item: noattr
# __getattr__ called item: noattr
# 'Err 404, 你请求的参数不存在'

