##  以下代码使用 shift + enter 执行
##  类属性和对象属性
# 示例-1
class Human(object):
    live = True
    def __init__(self, name):
        self.name = name

man = Human("Adam")
woman = Human("Eve")

Human.__dict__
man.__dict__
woman.__dict__

man.live
man.live = False

man.live
woman.live
Human.live

Human.__dict__
man.__dict__
woman.__dict__

woman.test = 'test'
woman.__dict__
##########################################
# 示例-2
class Person(object):
    age = 3
    def __init__(self, name):
        self.name = name

# 类型
Person.__class__
type(Person)
Person.__class__ is type(Person)

# 类字典
sorted(Person.__dict__.items())

## 通过实例访问类
tom = Person('Tom')  # 实例化一个实例
# 实例所属的类
tom.__class__
type(tom)
tom.__class__ is type(tom)

# 访问实例的类属性 __name__
tom.__class__.__name__
type(tom).__name__

# 访问实例的类属性 __dict__
sorted(tom.__class__.__dict__.items())
sorted(tom.__dict__.items())

'''
类属性保存在类的__dict__中， 实例属性保存在实例的__dict__中
如果从实例访问类的属性，可以能过__class__找到所属的类，再通过类来访问类属性
如:  tom.__class__.age
'''
################################
## 示例-3
class Person(object):
    age = 3
    height = 170

    def __init__(self, name, age=18):
        self.name = name

tom = Person('Tom')
jerry = Person('Jerry', 20) 

Person.age = 30
Person.age   # 30
tom.age      # 30
jerry.age    # 30


Person.height  # 170
tom.height     # 170
jerry.height   # 170

jerry.height = 175
Person.height  # 170
tom.height     # 170
jerry.height   # 175


tom.height += 10 
Person.height  # 170
tom.height     # 180
jerry.height   # 175


Person.height += 15
Person.height  # 185
tom.height     # 180
jerry.height   # 175

Person.weight = 70
Person.weight  # 70
tom.weight     # 70
jerry.weight   # 70


tom.__dict__['height']    # 180
tom.__dict__['weight']    # 报错: KeyError: 'weight'

sorted(Person.__dict__.items())
# [('__dict__', <attribute '__dict__' of 'Person' objects>), 
# ('__doc__', None), ('__init__', <function Person.__init__ at 0x7f8f4e15d320>), ('__module__', '__main__'), ('__weakref__', <attribute '__weakref__' of 'Person' objects>), 
# ('age', 30), ('height', 170), ('weight', 70)]

sorted(tom.__dict__.items())
# [('height', 180), ('name', 'Tom')]

sorted(jerry.__dict__.items())
# [('height', 175), ('name', 'Jerry')]

'''
总结：
是类的， 也是这个类的所有实例的， 其实例都可以访问得到
是实例的，就是这个实例自己的，通过类访问不到
类变量是属于类的变量，这个类的所有实例可以共享这个变量

对象（类或实例）可以动态的给自己增加一个属性（赋值即定义一个新属性）

实例.__dict__[变量名] 和 实例.变量名 都可以访问到实例自己的属性（但是有本质的区别）

实例的同名变量后隐藏掉类变量，或者说是覆盖这个类变量。但注意类变量还在那里，并没有被真正的被覆盖

'''

'''
实例属性的查找顺序：
当实例使用 . 来访问属性，会先找自己的__dict__, 如查没有，会通过属性 __class__ 找到自己的类，再去
类的__dict__中查找

注意：使用__dict__[变量名]访问变量，将不会按照上面的查找顺序查找变量，这是指明使用字典的KEY查找，不是
属性查找
'''

##########################
# 示例-4 
# 为类或实例增加属性

# 方法1- 赋值即定义一个新属性 使用 .属性名 = 值
class Human(object):
    live = True

    def __init__(self, name):
        self.name = name

Human.newattr = "new_attr"
Human.__dict__['newattr']   # 'new_attr'
dir(Human)
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', 
# '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', 
# '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', 
# '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
# '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 
# '__weakref__', 'live', 'newattr']

# 方法-2 ，使用 setattr(class, key, value)
class Human(object):
    live = True

    def __init__(self, name):
        self.name = name

setattr(Human, 'setnewattr', 'setnewvalue')
Human.__dict__["setnewattr"]    # 'setnewvalue'
dir(Human)  
#['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', 
# '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '
# __init__', '__init_subclass__', '__le__', '__lt__', '__module__', 
# '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
# '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 
# 'live', 'setnewattr']


# 内置类型不能增加属性和方法
setattr(list, "addattr", 'listadd')
# TypeError: can't set attributes of built-in/extension type 'list'


# ().__class__.__bases__[0].__subclasses__()
##########################################################################################
## 访问控制
# 私有成员
class Person:
    def __init__(self, name, age=18):
        self.__name = name
        self.__age = age

    def __showage(self):
        print(self.__age)

Person.__name  # AttributeError: type object 'Person' has no attribute '__name'
Person.__showage  # AttributeError: type object 'Person' has no attribute '__showage'

tom = Person('Tom')
tom.__name  # AttributeError: 'Person' object has no attribute '__name'
tom.__showage  # AttributeError: 'Person' object has no attribute '__showage'
 
# 私有成员本质
class Person:
    def __init__(self, name, age=18):
        self.__name = name
        self.__age = age

    def __showage(self):
        print(self.__age)

sorted(Person.__dict__.items())
# [('_Person__showage', < function Person.__showage at 0x7fe68f15da70 > ), 
# ('__dict__', < attribute '__dict__' of 'Person' objects > ), ('__doc__', None), 
# ('__init__', < function Person.__init__ at 0x7fe68f15d9e0 > ), ('__module__', '__main__'), 
# ('__weakref__', < attribute '__weakref__' of 'Person' objects > )]

tom = Person('Tom')
tom.__dict__   # {'_Person__name': 'Tom', '_Person__age': 18}
 
# 保护成员
class Person:
    def __init__(self, name, age=18):
        self._name = name
        self._age = age

    def _showage(self):
        print(self._age)

sorted(Person.__dict__.items())
# [('__dict__', <attribute '__dict__' of 'Person' objects>), ('__doc__', None), 
# ('__init__', <function Person.__init__ at 0x7fe68f15dc20>), ('__module__', '__main__'),
#  ('__weakref__', <attribute '__weakref__' of 'Person' objects>), 
# ('_showage', <function Person._showage at 0x7fe68f15dcb0>)]

tom = Person('Tom')
tom.__dict__  # {'_name': 'Tom', '_age': 18}
tom._name     # 'Tom'
tom._age      # 18


# 描述器
class Teacher():
    def __init__(self, name):
        self.name = name

    def __get__(self):
        return self.name

    def __set__(self, value):
        self.name = value

pythonteacher = Teacher('yin')
pythonteacher.name                  # 'yin'
pythonteacher.name = 'Yin'
pythonteacher.name                  # 'Yin'


## 示例 - 1
# 通过打印来显示描述器的访问流程
class Desc(object):
    def __init__(self, name):
        self.name = name

    # 固定的三个参数， instance 指实例，  owner 指实例所属的类
    def __get__(self, instance, owner):
        print(f'__get__{instance} {owner}')
        return self.name
    
    # 固定的三个参数， instance 指实例，  value 指set的值
    def __set__(self, instance, value):
        print(f'__set__{instance} {value}')
        self.name = value

    # 固定的2个参数， instance 指实例
    def __delete__(self, instance):
        print(f'__delete__ {instance}')
        del self.name

class MyObj(object):
    a = Desc('aaa')
    b = Desc('bbb')

my_object = MyObj()
my_object.a
# __get__ < __main__.MyObj object at 0x7f8469a42d50 > <class '__main__.MyObj' >
# 'aaa'

my_object.a = '456'
# __set__ < __main__.MyObj object at 0x7f8469a42d50 > 456

my_object.a
# __get__ < __main__.MyObj object at 0x7f8469a42d50 > <class '__main__.MyObj' >
# '456'

## porperty
class Human():
    def __init__(self,name):
        self.name = name

    # 将方法封装成属性
    @property
    def gender(self):
        return 'M'

h1 = Human("Adam")
h2 = Human("Eve")
h1.gender
# 'M'
h2.gender = "F"
# Traceback(most recent call last):
#   File "<stdin>", line 1, in <module >
# AttributeError: can't set attribute

# 示例 - 2
class Human2:
    def __init__(self):
        self._gender = None

    @property   # 将方法封装成属性
    def gender(self):
        print(self._gender)

    @gender.setter  # 支持修改
    def gender(self, value):
        self._gender = value

    @gender.deleter  # 支持删除
    def gender(self):
        del self._gender


h = Human2()
h.gender
# None
h.gender = "F"
h.gender
# F
del h.gender
h.gender
# Traceback(most recent call last):
#   File "<stdin>", line 1, in <module >
#   File "<stdin>", line 6, in gender
# AttributeError: 'Human2' object has no attribute '_gender'

# 上例的另一种方法
class Human3:
    def __init__(self):
        self._gender = None

    def get_(self):
        print(self._gender)

    def set_(self, value):
        self._gender = value

    def del_(self):
        del self._gender

    gender = property(get_, set_, del_)


h = Human2()
h.gender
# None
h.gender = "F"
h.gender
# F
del h.gender
h.gender
# Traceback(most recent call last):
#   File "<stdin>", line 1, in <module >
#   File "<stdin>", line 6, in gender
# AttributeError: 'Human2' object has no attribute '_gender'
