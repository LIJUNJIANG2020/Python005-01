# Redis

Redis 是一个性能非常高的非关系型数据库，大多数被当做缓存使用， 支持数据的持久化

特点：

- 使用IO多路复用机制
- 监听多个文件描述符实现读写事件
- 6.0以前为单作线程，6.0后支持多线程模式(单工作线程可能会导致多个会话间相互干扰)



## 安装

环境说明：

- 操作系统： CentOS 7  x86_64
- Redis 版本:  [redis-6.0.6.tar.gz](http://download.redis.io/releases/redis-6.0.6.tar.gz)
- gcc version : 8.0+ 

安装过程：

1. 安装gcc 

    ```sh
    # 安装
    yum install centos-release-scl scl-utils-build
    yum list all --enablerepo='centos-sclo-rh'
    yum install devtoolset-8-toolchain
    scl enable devtoolset-8 bash
    
    ####查看gcc 版本
    [root@geekbang ~]# gcc --version
    gcc (GCC) 8.3.1 20190311 (Red Hat 8.3.1-3)
    Copyright (C) 2018 Free Software Foundation, Inc.
    This is free software; see the source for copying conditions.  There is NO
    warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    
    ```

2. 安装redis

    ~~~sh
    # 下载
    wget http://download.redis.io/releases/redis-6.0.6.tar.gz
    
    # 解压
    tar zxvf redis-6.0.6.tar.gz && cd redis-6.0.6
    
    # 编译 && 安装
    make && make install PREFIX=/usr/local/redis  # PREFIX= 指定安装目录
    
    ### 查看
    [root@geekbang redis]# ls /usr/local/redis/bin/
    redis-benchmark  redis-check-aof  redis-check-rdb  redis-cli  redis-sentinel  redis-server
    
    ~~~

3. 配置

    ```sh
    # 在解压目录拷备配置文件模版
    mkdir /usr/local/redis/config
    cp redis.conf /usr/local/redis/config
    
    ## 常用配置项
    bind 0.0.0.0     # 绑定的ip
    port 6379		 # 监听端口
    requirepass *****  # 访问密码
    ```

4. 设置开机启动

    ```sh
    # 命令行启动
     /usr/local/redis/bin/redis-server /usr/local/redis/config/redis.conf
     
    # 设置为系统服务并开机自启
    cat << "EOF" > redis
    [Unit]
    Description=Redis persistent key-value database
    After=network.target
    After=network-online.target
    Wants=network-online.target
    
    [Service]
    ExecStart=/usr/local/redis/bin/redis-server /usr/local/redis/config/redis.conf --supervised systemd
    ExecStop=/usr/libexec/redis-shutdown
    Type=notify
    User=redis
    Group=redis
    RuntimeDirectory=redis
    RuntimeDirectoryMode=0755
    
    [Install]
    WantedBy=multi-user.target
    
    EOF
    ###############################
    ## 设置开机自启
    # 创建启动用户和组
    groupadd redis
    useradd -M -g redis -s /sbin/nologin redis 
    
    chmod 755 /usr/local/redis/config/redis.service
    ln -s /usr/local/redis/config/redis.service /etc/init.d/
    systemctl enable redis.service
    
    # 启动redis 服务
    systemctl start redis.service
    
    ### 查看服务
    [root@geekbang config]# ps aux|grep redis
    root      12043  0.0  0.1 115404  1480 ?        Ss   14:02   0:00 /bin/sh /etc/rc.d/init.d/redisd start
    root      12044  0.0  0.2 191876  2324 ?        S    14:02   0:00 su -s /bin/bash -c /usr/local/redis/bin/redis-server /usr/local/redis/config/redis.conf root
    root      12045  0.1  0.8 162392  8304 ?        Sl   14:02   0:00 /usr/local/redis/bin/redis-server 0.0.0.0:6379
    root      12124  0.0  0.0 112828   984 pts/0    R+   14:05   0:00 grep --color=auto redis
    
    ```

5. 连接redis

    ```
    [root@geekbang config]# /usr/local/redis/bin/redis-cli 
    127.0.0.1:6379> auth qwe123
    OK
    127.0.0.1:6379> get keys
    (nil)
    127.0.0.1:6379> 
    ```



## Redis 的对象类型

- 字符串
- 列表
- 哈希
- 集合
- 有序集合



## Python 操作 Redis

需要安装redis 模块

> pip installl redis

### 连接

```python
import redis

clinet = redis.Redis(host='10.0.0.128', port=6379, password='qwe123')
print(clinet)

print(clinet.keys())
for key in clinet.keys():
    print(key.decode())
####Out
Redis<ConnectionPool<Connection<host=10.0.0.128,port=6379,db=0>>>
[]
```

### 操作字符串

- set(key, value)  

    > Set the value at key ``name`` to ``value``

    ``ex``  sets an expire flag on key ``name`` for ``ex`` seconds.

    ``px``  sets an expire flag on key ``name`` for ``px`` milliseconds.

    ``nx``  if set to True, set the value at key ``name`` to ``value`` only  if it does not exist.

    ``xx``  if set to True, set the value at key ``name`` to ``value`` only  if it already exists.

    ``keepttl``  if True, retain the time to live associated with the key. (Available since Redis 6.0)

- get(key)

    > Return the value at key ``name``, or None if the key doesn't exist

- append(key, value)

    > Appends the string ``value`` to the value at ``key``. If ``key`` doesn't already exist, create it with a value of ``value``.  Returns the new length of the value at ``key``.

- incr(name, amount=1)

    > Increments the value of ``key`` by ``amount``.  If no key exists,  the value will be initialized as ``amount``

- decr( name, amount=1)

    > Decrements the value of ``key`` by ``amount``.  If no key exists, the value will be initialized as 0 - ``amount``

- 注意事项

    1. 适用于小量级的服务中，一般不要超过百万，超过的话建议使用哈希，哈希所占用的内存是字符串的1/4大小，且查询效率基本一样
    2. 当数据量较大时，不要使用keys * 的方式查询所有，当keys * 执行时，redis会列出所有的key值，这一过程会导致其redis操作短暂失去响应

```python
import redis


client = redis.Redis(host="10.0.0.128", port=6379, password='qwe123')

client.set('key', 'value')

result = client.get('key')

print(f'get: {result}')

client.append('key', 'add')
print(f'append: {client.get("key")}')
####
client.set('key2', 100)
res = client.incr('key2')
print(f'incr: {res}')
res = client.decr('key2')
print(f'derc: {res}')

##### OUT
get: b'value'
append: b'valueadd'
incr: 101
derc: 100
```

### 操作列表

在redis中列表一般做为队列来使用， 有索引从0开始进行编号且支持负索引，做为队列使用时通过队列左侧右侧进行取分，左侧第一个元素索引为0 ， 右侧第一个元素的索引为 -1

- 获取列表长度

    - llen(name)

        > Return the length of the list ``name``

- 插入数据

    - lpush(name, *values)  左侧插入

        > Push ``values`` onto the head of the list ``name``

    - rpush(name, *values)  右侧插入

        > Push ``values`` onto the tail of the list ``name`

- 弹出数据

    - lpop(name)

        > Remove and return the first item of the list ``name``

    - rpop(name)

        > Push ``values`` onto the head of the list ``name``

- 查看指定范围的数据

    - lrange(name, start, end)

        > Return a slice of the list ``name`` between position ``start`` and ``end``
        >
        >  ``start`` and ``end`` can be negative numbers just like  Python slicing notation

```python
import redis

client = redis.Redis(host="10.0.0.128", port=6379, password="qwe123")

demo = 'list_demo'

# # 插入数据
# client.lpush(demo, 'python')
# client.rpush(demo, 'java')

# # 查看长度
# print(client.llen(demo))

# # 弹出数据
# print(client.llen(demo))
# l_res = client.lpop(demo)
# r_res = client.rpop(demo)
# print(f"l_res: {l_res}")
# print(f"r_res: {r_res}")
# print(client.llen(demo))

# # 查看一定范围的数据
# res = client.lrange(demo, 0, -1)
# print(f"lrang: {res}")

# # 示例
import random
users = range(0, 10)
users = client.rpush('users', *users)
# print(client.lrange('users', 0,-1))

def send(user):
    num = random.choice(range(0, 2))
    if num:
        print(f"user: {user} is Error...")
        return False
    else:
        print(f"user: {user} is Ok...")
        return True

while True:
    user = client.rpop('users')
    if user == None:
        print("send over")
        break
    if not send(user.decode()):
        client.lpush('users', user)
```

### 集合操作

Redis集合是一个无序的字符串集合。集合内的元素不重复，且没有顺序

- sadd( name, *values)

    > Add ``value(s)`` to set ``name``

- smembers(nane)

    >Return all members of the set ``name``

- spop(name, count=None)

    >Remove and return a random member of set ``name``

- siniter(keys, *args)  交集

    > Return the intersection of sets specified by ``keys``

- sunion(keys, *args) 并集

    >Return the union of sets specified by ``keys``

- sdiff(keys, *args)  差集

    >Store the difference of sets specified by ``keys`` into a new set named ``dest``.  Returns the number of keys in the new set.

```python
import redis
client = redis.Redis(host="10.0.0.128", port=6379, password="qwe123")

# sadd() 向集合插入数据
print(client.sadd('set_demo', 'data1'))
print(client.sadd('set_demo', 'data2'))

print(client.smembers('set_demo'))

# spop() 随机弹出集合中一条数据
# print(client.spop('set_demo'))

# smembers() 查看集合中的数据
# print(client.smembers('set_demo'))

data = ['data2', 'data3']
client.sadd('set_demo1', *data)
print(client.smembers("set_demo1"))

print(client.sinter('set_demo1', 'set_demo'))   # 求交集
print(client.sunion('set_demo1', 'set_demo'))   # 求并集
print(client.sdiff('set_demo', 'set_demo1'))    # 求差集
print(client.sdiff('set_demo1', 'set_demo'))

''' Out
0
0
{b'data1', b'data2'}
{b'data3', b'data2'}
{b'data2'}
{b'data3', b'data1', b'data2'}
{b'data1'}
{b'data3'}
'''
```



### 哈希操作

​	需要注意返回值

- hset(name, key=None, value=None, mapping=None)

    >Set ``key`` to ``value`` within hash ``name``,  ``mapping`` accepts a dict of key/value pairs that that will be added to hash ``name``.
    >
    >Returns the number of fields that were added.

- hdel(name, key)

    >Return the value of ``key`` within the hash ``name``

- hexists(name, key)

    > Returns a boolean indicating if ``key`` exists within hash ``name``

- hmset(name, mapping)

    > Set key to value within hash ``name`` for each corresponding key and value from the ``mapping`` dict.

- hkeys(name)

    > Return the list of keys within hash ``name``

- hget(name, key)

    >Return the value of ``key`` within the hash ``name``

- hmget(name, )

    > Returns a list of values ordered identically to ``keys``

- hgetall(name)

    > Return a Python dict of the hash's name/value pairs

```python
import redis

client = redis.Redis(host='10.0.0.128', port=6379, password='qwe123')

client.hset('hash_demo', key='key1', value='value1')  # 插入一个值
client.hset('hash_demo', 'key2', 'value2')      
print(client.hget('hash_demo', 'key1'))   # 获取一个key的值
print(client.hget('hash_demo', 'key2'))
print(client.hgetall('hash_demo'))        # 获取所有key value对

print(client.hdel('hash_demo', 'key2'))   # 删除一个键值对

print(client.hexists('hash_demo', 'key1'))  # 查询某个键时否存在
print(client.hexists('hash_demo', 'key2'))
print(client.hgetall('hash_demo'))         # 获取所有的键值对
'''Out
b'value1'
b'value2'
{b'key1': b'value1', b'key2': b'value2'}
1
True
False
{b'key1': b'value1'}
'''

data = {'key2': 'value2',
        'key3': 'value3',
        'key4': 'value4',
        'key5': 'value5',
    }

# 插入多个值
client.hmset('hash_demo', data)
# 获取所有keys
print(client.hkeys('hash_demo'))
# 获取多个key
print(client.hmget('hash_demo', 'key1', 'key2', 'key5'))
# 获取所有key value对
print(client.hgetall('hash_demo'))
'''Out
[b'key1', b'key3', b'key4', b'key5', b'key2']
[b'value1', b'value2', b'value5']
{b'key1': b'value1', b'key3': b'value3', b'key4': b'value4', b'key5': b'value5', b'key2': b'value2'}
'''
```



### 有序集合操作

​	插入和查询与数据量正相关，数据量越大插入和查询的时间越长

​	具有不重复性、排序 

- zadd(name, mapping)
- zincrby(name, value, key)
- zrangebyscore(name, min, max， start， end)
- zrevrank()
- zcard(name)
- zrange(name, start, end, withscores=True)
- zrevrange(name, start, end, withscores=True)

