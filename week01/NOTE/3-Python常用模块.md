# Python 常用模块

[标准库](https://docs.python.org/zh-cn/3.7/library/index.html)

## [time](https://docs.python.org/zh-cn/3.7/library/time.html)

>时间的访问和转换

~~~python
import time

time.time()

time.localtime()

time.strftime(%Y-%m-%d %X, time.localtime())

time.strptime("2020-11-26 16:59:15", %Y-%m-%d %X)

~~~

## [datetime](https://docs.python.org/zh-cn/3.7/library/datetime.html)

> 基本的日期和时间类型

~~~python
import datrtime

datetime.datetime.today()
#############################################
form datetime import *

datetime.today()
datetime.now()

datetime.today() - timedelta(days=1)
datetime.today() + timedelta(days=-1)

#timedelta 类对象

~~~



## [logging](https://docs.python.org/zh-cn/3.7/library/logging.html)

> python 的日志记录工具

#### 日志级别

- info
- warning
- error
- debug
- critical

~~~python
In [1]: import logging                                                                                                                                                           

In [2]: logging.debug('This is debug message')                                                                                                                                   

In [3]: logging.info('This is info message')                                                                                                                                     

In [4]: logging.warning('This is warning message')                                                                                                                               
WARNING:root:This is warning message

In [5]: logging.error('This is error message')                                                                                                                                   
ERROR:root:This is error message

In [6]: logging.critical('This is critical message')                                                                                                                             
CRITICAL:root:This is critical message

~~~

#### 配置

- `logging.basicConfig`(***kwargs*)[¶](https://docs.python.org/zh-cn/3.7/library/logging.html#logging.basicConfig)

    常用键字参数：

    ​	filename：使用指定的文件名而不是 StreamHandler 创建 FileHandler

    ​	datefmt：使用指定的日期/时间格式，与 [`time.strftime()`](https://docs.python.org/zh-cn/3.7/library/time.html#time.strftime) 所接受的格式相同。

    ​	level： 设置根记录器级别去指定 [level](https://docs.python.org/zh-cn/3.7/library/logging.html#levels).

- LogRecord 属性[¶](https://docs.python.org/zh-cn/3.7/library/logging.html#logrecord-attributes)

    常用属性

    ​	asctime

    ​	levelname

    ​	lineno

    ​	message

~~~python
In [1]: import logging                                                                                                                                                           

In [2]: logging.basicConfig(filename="/tmp/test.log")                                                                                                                            

In [3]: logging.info('This is info message') 
   ...: logging.warning('This is warning message') 
   ...: logging.error('This is error message') 
   ...: logging.critical('This is critical message') 
   ...: logging.debug('This is debug message')                                                                                                                                   

In [4]: !cat /tmp/test.log                                                                                                                                                       
WARNING:root:This is warning message
ERROR:root:This is error message
CRITICAL:root:This is critical message
###################################################################

In [1]: import logging                                                                                                                                                           

In [2]: logging.basicConfig(filename="/tmp/test1.log", 
   ...:                     level=logging.DEBUG, 
   ...:                     datefmt='%Y-%m-%d %H:%M:%S', 
   ...:                     format='%(asctime)s %(name)-8s %(levelname)-8s [line: %(lineno)d] %(message)s')                                                                      

In [3]: logging.info('This is info message') 
   ...: logging.warning('This is warning message') 
   ...: logging.error('This is error message') 
   ...: logging.critical('This is critical message') 
   ...: logging.debug('This is debug message')                                                                                                                                   

In [4]: !cat /tmp/test1.log                                                                                                                                                      
2020-11-26 18:15:42 root     INFO     [line: 1] This is info message
2020-11-26 18:15:42 root     WARNING  [line: 2] This is warning message
2020-11-26 18:15:42 root     ERROR    [line: 3] This is error message
2020-11-26 18:15:42 root     CRITICAL [line: 4] This is critical message
2020-11-26 18:15:42 root     DEBUG    [line: 5] This is debug message


~~~



## [random](https://docs.python.org/zh-cn/3.7/library/random.html)

> 生成伪随机数

~~~python
from random import *
In [9]: randrange(0, 101, 2)  # 重成随机偶数                                                    
Out[9]: 66

In [10]: randrange(0, 101)    # 生成0-100 的随机数                                              
Out[10]: 60

In [11]: randrange(0, 101, 2)  # 生成0-100的随机偶数                                            
Out[11]: 20

In [13]: random() # 生成0.0到1.0的随机伪浮点数（跟据当前时间戳）                                
Out[13]: 0.4161178754105419

In [14]: choice(["red", "blue", "orange"])                                                      
Out[14]: 'orange'

In [15]: choice(["red", "blue", "orange"])                                                      
Out[15]: 'blue'

In [16]: choice(["red", "blue", "orange"]) #                           
Out[16]: 'orange'

In [17]: choice(("red", "blue", "orange")) # 随机先择一个元素      
Out[17]: 'orange'
    
In [18]: sample([1, 2, 3, 4, 5], k=4)                                                           
Out[18]: [3, 5, 2, 1]

In [19]: sample([1, 2, 3, 4, 5], k=4)                                                           
Out[19]: [4, 3, 5, 1]

In [20]: sample((1, 2, 3, 4, 5), k=4)                                                           
Out[20]: [2, 4, 5, 3]

In [21]: sample((1, 2, 3, 4, 5), k=4)   # 随机抽取指定的个数的元素                                                        
Out[21]: [3, 5, 4, 1]
  

~~~



## [json](https://docs.python.org/zh-cn/3.7/library/json.html)

>JSON 编码和解码

~~~python
In [1]: import json
    
In [3]: json.loads('["foo", {"bar": ["baz", null, 1.8, 2]}]')       # json.loads 解码                      
Out[3]: ['foo', {'bar': ['baz', None, 1.8, 2]}]

In [4]: json.dumps("['foo', {'bar': ['baz', None, 1.8, 2]}]")       # json.dumps 编码                  
Out[4]: '"[\'foo\', {\'bar\': [\'baz\', None, 1.8, 2]}]"'

In [5]:       
~~~



## [pathlib](https://docs.python.org/zh-cn/3.7/library/pathlib.html)

>面向对象的文件系统路径，对文件、目录进行处理

~~~python
In [1]: from pathlib import Path                                                         

In [2]: p = Path()      # 实例化                                                                 
In [3]: p.resolve()     # 显示当前所在的完整路径                                                                 
Out[3]: PosixPath('/Users/lijunjiang')
    
########
In [1]: from pathlib import Path                                                

In [2]: path = "/usr/local/a.txt.py"      # 定义要处理的文件路径                                      
	
In [3]: p = Path(path)                    # 实例化Path并传入要处理的文件路径                                      

In [4]: p                                 #                            
Out[4]: PosixPath('/usr/local/a.txt.py')

In [5]: p.name                            # 获取文件名                                  
Out[5]: 'a.txt.py'

In [6]: p.stem                            # 获取无后缀的文件名                         
Out[6]: 'a.txt'

In [7]: p.suffix                          # 获取文件后缀                     
Out[7]: '.py'

In [8]: p.suffixes                        # 获取多后缀文件的后缀， 如 *.tar.gz *tar.bz2                          
Out[8]: ['.txt', '.py']

In [9]: p.parent                          # 获取文件的路径
Out[9]: PosixPath('/usr/local')

In [10]: p.parents                        # 获取文件路径 可迭代对象                        
Out[10]: <PosixPath.parents>

In [11]: for i in p.parents: 			  # 迭代路径对象，对多级路径进行处理
    ...:     print(i) 
    ...:                                                                        
/usr/local
/usr
/

In [12]: p.parts                          # 以元组形式对路径进行分割                             
Out[12]: ('/', 'usr', 'local', 'a.txt.py')
    

~~~



## [os.path](https://docs.python.org/zh-cn/3.7/library/os.path.html)

> 常见路径操作

~~~python
In [17]: import os                                                              

In [18]: cd /tmp                                                                
/private/tmp

In [20]: os.path.abspath('text1.log')               # 获取给定文件的完整路径                            
Out[20]: '/private/tmp/text1.log'

In [21]: path = "/usr/local/a.txt"                                     

In [22]: os.path.basename(path)                     # 获取给定文件路径的文件名                 
Out[22]: 'a.txt'

In [23]: os.path.dirname(path)                      # 获取给定文件路径的路径      
Out[23]: '/usr/local'

In [24]: os.path.exists('/etc/hosts')               # 判断文件或目录是否存在        
Out[24]: True

In [25]: os.path.exists('/etc/host')                  
Out[25]: False

In [26]: os.path.isfile('/etc/host')                 # 判断给定路径是否为文件                          
Out[26]: False

In [27]: os.path.isfile('/etc/hosts')                                        
Out[27]: True

In [28]: os.path.isdir('/etc/hosts')                 # 判断给定路径是否为目录          
Out[28]: False

In [29]: os.path.join("a", "b")                      # 拼接路径       
Out[29]: 'a/b' 
~~~



## [re](https://docs.python.org/zh-cn/3.7/library/re.html)

> 正则表达式操作  检索  替换 提取子串

- 元字符

    > 待总结 

- re.complie(pattern, flags=0)    将正则表达式编译成一个正则表达式对象，可以用于匹配，通过这个对象的方法进行操作

    两种模式：

    >		```python
    >		1、使用正则对象
    >		prog = re.complie(pattern)
>		result = prog.match(string)
    >		```

    等价于
    
    > 2、使用正则方法
>
    > result = re.match(pattern, string)  

    1、需多次使用同一个正则表达式时，使用re.complie()并保存这个正则对象以便复用，可使程序更高效
    
    2、通过re.complie() 的对象编译后会被缓存， 少数的正则表达式使用无需考虑编译问题
    
- 常用re 方法  

    - re.match()

        - 完全匹配

        ~~~python
        In [1]: import re                                                               
        
        In [2]: content = "13210010001"                                                 
        
        In [4]: re.match('.{11}', content)            # 完全匹配                                  
        Out[4]: <re.Match object; span=(0, 11), match='13210010001'>
        
        In [5]: re.match('^1[3-9][0-9]{9}$', content)                                    
        Out[5]: <re.Match object; span=(0, 11), match='13210010001'>
        
        In [6]: re.match('^1[3-9][0-9]{9}$', "12312312312")                              
        
        In [7]: re.match('^1[3-9][0-9]{9}$', "132212312312")     
            
        #####
        In [11]: re.match('^1[3-9]+[0-9]{9}$', "13221231231").group()    # 取出匹配字符串                 
        Out[11]: '13221231231'
        
        In [12]: re.match('1[3-9]+[0-9]{9}', "23232313221231231009090").span()     # 获取匹配字串的范围
        Out[12]: (0, 11)
        ######
        In [33]: re.match('(^1[3-9][0-9])([0-8]{4})([0-9]{4})$', "13221231231").groups() # 对匹配字段分组，获取所有
            ...:                                                                        
        Out[33]: ('132', '2123', '1231')
        
        In [35]: re.match('(^1[3-9][0-9])([0-8]{4})([0-9]{4})$', "13221231231").group(1) # 获取第一个
            ...:                                                                        
        Out[35]: '132'
        
        In [36]: re.match('(^1[3-9][0-9])([0-8]{4})([0-9]{4})$', "13221231231").group(2) # 获取第二个
            ...:                                                                        
        Out[36]: '2123'
        
        In [37]: re.match('(^1[3-9][0-9])([0-8]{4})([0-9]{4})$', "13221231231").group(3) # 获取第三个
            ...:                                                                        
        Out[37]: '1231'
        
        ~~~

    - re.search()

        - 扫描整个字符串并返回第一个匹配的字串

        ~~~python
        In [38]: re.search('@', '123@123.com')                                          
        Out[38]: <re.Match object; span=(3, 4), match='@'>
        
        In [39]: re.search('@', '123@123.com').group()                                  
        Out[39]: '@'
        
        In [40]: re.search('@', '123@123.com').span()                                   
        Out[40]: (3, 4)
        ~~~

    - re.findall()

        - 扫描整个字段并返回所有匹配字串

        ~~~python
        In [41]: re.findall('@', '123@123.com')                                         
        Out[41]: ['@']
        
        In [43]: re.findall('123', '123@123.com')                                       
        Out[43]: ['123', '123']
        
        ~~~

    - re.sub()

        - 扫描整个字段并替换所有匹配字串

        ~~~python
        In [44]: re.sub('123', '456', '123@123.com')  #将字段中的每个123字串替换成 456                                  
        Out[44]: '456@456.com'
        
        In [45]: re.sub('\d', 'xyz', '123@123.com')   # 将字段中的每个数字替换成 xyz      
        Out[45]: 'xyzxyzxyz@xyzxyzxyz.com'
        
        In [46]: re.sub('\d+', 'xyz', '123@123.com')  # 将字段中的每一个连续的数字串替换成 xyz                 
        Out[46]: 'xyz@xyz.com'
        ~~~

    - re.split()

        - 将字段按指定字串进行分割

        ~~~python
	    In [47]: re.split('@', '123@123.com')     # 按指定字串对字段进行分串，结果不包念指定字串                                       
        Out[47]: ['123', '123.com']
        
        In [48]: re.split('(@)', '123@123.com')   # 按指定字串对字段进行分串，结果包念指定字串
        Out[48]: ['123', '@', '123.com']
        ~~~
    
        
    
         

​    

