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

~~~

~~~



## [json](https://docs.python.org/zh-cn/3.7/library/json.html)

>

## [pathlib](https://docs.python.org/zh-cn/3.7/library/pathlib.html)

>

## [os.path](https://docs.python.org/zh-cn/3.7/library/os.path.html)

>

## [re](https://docs.python.org/zh-cn/3.7/library/re.html)

>

