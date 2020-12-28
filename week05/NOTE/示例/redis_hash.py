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