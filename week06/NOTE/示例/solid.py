## 通过装饰器实现单实例
def singleton(cls):
    instance = {}
    def getinstance():
        if cls not in instance:
            instance[cls] = cls()
        return instance[cls]
    return getinstance

@singleton
class MyClass:
    pass

m1 = MyClass()
m2 = MyClass()

id(m1), id(m2)
# (140268130381392, 140268130381392)


# ``__new__`` 和 ``__init__`` 实例化过程
class Foo(object):
    def __new__(cls, name):
        print('trace __new__')
        return super().__new__(cls)

    def __init__(self, name):
        print('trace __init__')
        super().__init__()
        self.name = name


bar = Foo('test')
# trace __new__
# trace __init__
bar.name
# 'test'

## __new__ 方式实现单实例模式
class Singleton2(object):
    __isinstance = False # 默认没有实例化
    def __new__(cls, *args, **kwargs):
        if cls.__isinstance:
            return cls.__isinstance # 返回实例化对象
        cls.__isinstance = object.__new__(cls)
        return cls.__isinstance

'''
object 定义了一个名为Singleton的单例，它满足单例的3个要素
1. 只能有一个实例
2. 必须自行创建这个实例
3. 必须自行向整个系统提供这个实例
'''

## 使有import 实现

#############################
#
# 简单工厂模式（静态）
# 三个部分：
#    1、工厂角色
#    2、抽像产品角色，提供公共的接口
#    3、具体产品
#############################

# 抽像产品角色，提供公共的接口
class Human(object):
    def __init__(self):
        self.name = None
        self.gender = None
   
    def getName(self):
        return self.name

    def getGender(self):
        return self.gender

# 具体产品
class Man(Human):
    def __init__(self, name):
        print(f'Hi, man {name}')
# 具体产品
class Woman(Human):
    def __init__(self, name):
        print(f'Hi, woman {name}')


# 工厂角色
class Factory:
    def getPerson(self, name, gender):
        if gender == 'M':
            return Man(name)

        elif gender == 'F':
            return Woman(name)
        else:
            pass
factory = Factory()
person = factory.getPerson("Andm", "M")
person.getName()


#############################
#
# 类工厂模式（动态）
#
#############################

def factory2(func):
    class klass: pass # 创建一个空类
    # print(func, func.__name__)
    setattr(klass, func.__name__, func)  # 为类添加实例方法
    # setattr(klass, func.__name__, classmethod(func)) # 添加类方法
    # setattr(klass, func.__name__, staticmethod(func)) # 添加静态方法
    return klass 

def say_foo(self):  # 传入factory2的函数，注意第一个参数是self, 是一个类方法
    print('bar')


Foo = factory2(say_foo)  # 动态生成一个类
foo = Foo()              # 创建类的实例
foo.say_foo()            # 调用实例方法


#############################
#
# 元类
#    创建类的类
#
#############################

'''
- 元类是创建类的类，是类的模板
- 元类是用来控制如何创建类的，正如类是创建对象的模板一样
- 元类的实例为类，正如类的实例为对象
- 创建元类的两种方法
  1. class
  2. type
     - type（类名，父类的元组，包含属性的字典）
'''

# 使用type 创建类
# 元类type首先是一个类，所以比类工厂的方法更灵活多变，可以自由创建子类来扩展元类的能力
def hi():
    print('Hi, metaclass')

# type的三个参数： 类名，父类的元组，类的成员
Foo = type('Foo', (), {'say_hi': hi})
a = Foo             # 没有进和Foo实例化
a.say_hi()


## 示例-2

def pop_value(self, dict_value):
    for key in self.keys():
        if self.__getitem__(key) == dict_value:
            self.pop(key)
            break

# 元类要求，必须继承自type
class DelValue(type):
    # 元类要求，必须实现__new__方法
    def __new__(cls, name, base, attrs):
        attrs['pop_value'] = pop_value
        return type.__new__(cls, name, base, attrs)

class DelDictValue(dict, metaclass=DelValue):
    # python2的用法，在Python3中不支持
    # __metaclass__ = DelValue
    pass


d = DelDictValue()
d['a'] = "A"
d['b'] = "B"
d['c'] = "C"
d['d'] = "D"

d.pop_value("C")

for k, v in d.items():
    print(k, v)


a = 123
b = 123
c = a

id(a)
id(b)
id(c)

a = 456
id(a)
c = 789
id(c)
c = b = a

id(a)
id(b)
id(c)

x = [1, 2, 3]
id(x)
y = x
id(y)
x.append(4)
x
y
id(x), id(y)


a = [1, 2, 3]
id(a)
b = a
id(b)
a = [4, 5, 6]
a, b
id(a), id(b)


a = [1, 2, 3]
b = a
a, b
id(a), id(b)
a[0], a[1], a[2] = 4, 5, 6
a, b
id(a), id(b)

'''
python一切皆对象，传递的都是对象，不同的是有的是传递对象本身，有的传递的是对象的引用
据此可以将变量赋值分为：
- 可变数据类型
  > 传递对象的引用
    - 列表 list
    - 字典 dict
    
    值的变化不会新建对象，但对象的内容会发生变化

- 不可变数据类型
  > 传递对象本身
    - 整型 int
    - 浮点型 float
    - 字符串型 string
    - 元组 tuple

    在内存中不管有多少个引用都是相同的对象，只占一块内存空间
    当对变量进行运算改变变量引用对象的值的进候，需要新创建对象，可能会大量消耗内存空间
'''


'''
- 序列

    - 容器序列
      能存放不同类型的数据
        - list
        - tuple
        - collections.deque

    - 扁平序列
      存放的是相同类型的数据且只能容纳一种类型
        - str
        - bytes
        - bytearray
        - memoryview(内存视图)
        - array.array


- 深、浅拷备
    - 非容器序列不存在拷备的问题

'''
old_list = [ i for i in range(1, 11)]
print(old_list)
id(old_list)

new_list = old_list
# print(new_list)
# id(new_list)

new_list2 = list(old_list)
# print(new_list2)
# id(new_list2)

new_list3 = old_list[:]
# print(new_list3)
# id(new_list2)

old_list.append([11, 12])
print(old_list), id(old_list)
print(new_list), id(new_list)
print(new_list2), id(new_list2)
print(new_list3), id(new_list3)






