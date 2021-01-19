# solid 设计原则
- 单一责任原则 The Single Responsibility Principle （一个类只负责一个功能）
- 开放封闭原则 The Open Close Principle (对扩展开放，对修改封闭)
- 里氏替换原则 The Liskov Substitution Principle （子类需要完整的覆盖父类的方法）
- 依赖倒置原则 The Dependency Inversion Principle (不适用于Python)
- 接口分离原则 The Interface Segregation Principle (不适用于Python)



# 设计模式
用来解决一些普遍性的问题并保证结构完整
## 单例模式
1. 对象只存在一个实例
2. ``__init__``（初始化方法）和 ``__new__``（构造函数）的区别
    - ``__new__`` 是实例创建之前被调用，返回该实例对象，是静态方法
    - ``__init__`` 是实例对象创建完成后被调用的，是实例方法
    - ``__new__`` 先被调用，``__init__`` 后被调用
    - ``__new__`` 的返回值（实例）将传递给``__init__`` 方法的第一个参数， ``__init__``给这个实例设置相关参数
### 实现单实例
- 通过装饰器实现
```python
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
```

- 通过``__new__`` 和 ``__init__`` 方式实现单实例模式
```python
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
```
- 使用import实现单实例
```python

```
## 工厂模式
对类进行解耦

### 简单工厂模式
```python

```