# 异常捕获

```python
tyr:
	....
except:
	....
finly:  # 无论异常处理于否，都会执行下面的代码
	....
```

- 异常不等于错误

- 异常处理机制的原理

    - 异常是一个类
        - 异常捕获过程：
            1. 异常类把错误消息打包到一个对象(Traceback 对象)
            2. 然后该对象会自动查找到调用栈
            3. 直到运行系统找到明确声明如何处理这些类异常的位置

- Traceback

    > 异常追踪  产生错误的函数调用过程，显示了出错的位置，显示的顺序和异常信息对象传播的方向相反

- 所有异常继承自BaseException

- 异常信息与异常捕获

    - 异常信息在Traceback 信息的最后一行，有不同的类型

    - 捕获异常使用 try...except 语法

        - 捕获所有的异常

            ```python
            try:
            	...
            except Exception as e:   # 捕获所有的异常
            	...
            ```

        - 捕获特定的异常

            ~~~python
            try:
            	....
            except IOError:    # 捕获IOError异常
            	...
            ~~~

            

    - try...except 支持多重导常外理

        ~~~python
        try:
        	...
        except Exception as e:
        	try:
        		...
        	except Exception as f:
        		...
        	...
        ~~~

    - 当需要捕获多个异常时，如果已捕获其中一种异常，如果其它异常再次发生，程序不会去捕获，需要注意

- 常见异常类型

    - LookupEorror 下的 indexError 和 KeyError
    - IOError
    - NameError
    - TypeError
    - AttributeError
    - ZeroDivisionError

- 自定义异常

    ```python
    # 所有异常继承自BaseException, 但自定义异常需要继承 Exception 这个类
    class UserInputError(Exception):
        def __init__(self, ErrorInfo):
            super().__init__(self, ErrorInfo)
            self.errorinfo = ErrorInfo
        def __str__(self):
            return self.errorinfo
    
    
    userinput = 'a'
    
    try:
        if (not userinput.isdigit()):
            raise UserInputError('用户输入错误')
    except UserInputError as ue:
        print(ue)
    
    finally:
        del userinput
        
    '''
    (base) ➜  Python005-01 git:(main) ✗ /Users/lijunjiang/opt/anaconda3/bin/python3.8 /Users/lijunjiang/Study/文档/Python005-01/week02/NOTE/示例/inpuerr.py
    用户输入错误
    '''
    ```

    

- raise 抛出异常

## 异常优化

- 安装 pretty_errors

    > pip install pretty_errors

- 导入

    > import pretty_errors

```python
import pretty_errors
def foo():
	1/0

foo()

'''
(base) ➜  Python005-01 git:(main) ✗ /Users/lijunjiang/opt/anaconda3/bin/python3.8 /Users/lijunjiang/Study/文档/Python005-01/week02/NOTE/示例/inpuerr.py

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
inpuerr.py 26 <module>
foo()

inpuerr.py 24 foo
1/0

ZeroDivisionError:
division by zero
'''
```



# with 

> 上下文协议

```python
class Open:
    def __enter__(self):
        print('open')

    def __exit__(self, type, value, trace):
        print('close')

    def __call__(self):
        pass

with Open() as f:
    pass

'''
(base) ➜  Python005-01 git:(main) ✗ /Users/lijunjiang/opt/anaconda3/bin/python3.8 /Users/lijunjiang/Study/文档/Python005-01/week02/NOTE/示例/With_Open.py
open
close
(base) ➜  Python005-01 git:(main) ✗ 
'''
```

# 重构

- 第一版

    ```python
    import requests
    
    url = "https://movie.douban.com/top250"
    
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36'
    
    hearde = {'user-agent': user_agent}
    
    response = requests.get(url, headers=hearde)
    
    ```

- 第二版

    ```python
    import requests
    import sys
    from pathlib import Path
    
    url = "https://movie.douban.com/top250"
    
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36'
    
    header = {'user-agent': user_agent}
    try:    
        response = requests.get(url, headers=header)
    except requests.exceptions.ConnectTimeout as e:
        print('requests库超时')
        sys.exit(1)
    
    
    # 存储html文件路径及文件
    file_path = Path(__file__).resolve().parent  # 获取脚本所在位置的路径
    html_path = file_path.joinpath('html')      # 设置html存储文件所在路径
    if not html_path.is_dir():                      
        Path.mkdir(html_path)
    page = html_path.joinpath('douban.html')     # 设置html文件路径
    
    
    try:
        with open(page, 'w', encoding='utf-8') as f:
            f.write(response.text)
    except FileNotFoundError as e:
        print('文件无法打开')
    except IOError as e:
        print('文件读写错误')
    except Exception as e:
        print(f'其它错误 {e}')
    ```

# Python 编程规范

- PEP-8
- Google Python Style

