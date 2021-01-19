##  object 和 type 的父类及继承关系
object.__class__
# <class 'type' >
object.__bases__
# ()

type.__class__
# <class 'type' >
type.__bases__
# (<class 'object'>,)

## 
class People:
    def __init__(self):
        self.gene = 'XY'
    
    def walk(self):
        print('I can walk')


class Man(People):
    def __init__(self, name):
        self.name = name
    
    def work(self):
        print('I can work')

class Woman(People):
    def __init__(self, name):
        self.name = name

    def shopping(self):
        print('buy buy buy...')


p1 = Man('Adam')
p2 = Woman('Eve')
############################################
# gene 有没有被继承
p1.gene
'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Man' object has no attribute 'gene'
'''
class People:
    def __init__(self, name):
        self.gene = 'XY'
        self.name = name
    
    def walk(self):
        print('I can walk ')


class Man(People):
    def __init__(self, name):
        # 执行父类中__init__方法
        super().__init__(name)

    def work(self):
        print('work hard')

class Woman(People):
    def __init__(self, name):
        # 执行父类中__init__方法
        super().__init__(name)

    def shopping(self):
        print("buy buy buy...")

p1 = Man('Adam')
p2 = Woman('Eve')

p1.gene, p2.gene
# ('XY', 'XY')

p1.walk(), p2.walk()

## people有父类是谁
People.__bases__, People.__class__
# ((<class 'object'>,), <class 'type'>)

## 能否实现多重继承


# 能否实现多个父类同时继承
class sun(Man, Woman):
    pass

# 钻石继承
class BaseClass(object):
    num_base_calls = 0
    def call_me(self):
        print("Calling methed on Base Class")
        self.num_base_calls += 1

class LeftSubclass(BaseClass):
    num_left_calls = 0
    def call_me(self):
        print('Calling method on Left Class')
        self.num_left_calls += 1

class RightSubclass(object):
    num_right_calls = 0
    def call_me(self):
        print('Calling method on Right Class')
        self.num_right_calls += 1

class Subclass(LeftSubclass, RightSubclass):
    pass

a = Subclass()
a.call_me()

# Calling method on Left Class

## MRO （多重继承的顺序问题）
Subclass.mro()
# [ < class '__main__.Subclass' > , < class '__main__.LeftSubclass' > , 
# < class '__main__.RightSubclass' > , < class '__main__.BaseClass' > , 
# < class 'object' > ]

'''
手动分析多继承的顺序问题： 有向无环路图（DAG）
DAG原本是一种数据结构，因为DAG的拓扑结构带来的优异特性，经常被用于处理动态规则、寻求最短路径的场景

由入度为0的节点开始依次分析， 从左到右开始查找
当存在多个入度为零的节点时，左侧节点优先

                       object
        baseclass
            leftsubclass    rightsubclass
                       subclass

'''
改写
class LeftSubclass(BaseClass):
    num_left_calls = 0
    # def call_me(self):
    #     print('Calling method on Left Class')
    #     self.num_left_calls += 1
a = Subclass()
a.call_me()
# Calling method on Right Class

当涉及到钻石继承的时候，新式类采用的广度优先，古典类用的是深度优先

'''
# python 不支持重载
