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