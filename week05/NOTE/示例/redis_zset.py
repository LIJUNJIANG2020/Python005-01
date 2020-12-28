import redis

client = redis.Redis(host='10.0.0.128', password='qwe123')

data = {
    'a': 1,
    'b': 2, 
    'c': 4,
    'd': 3,
    'e': 5
}
client.zadd('zset', data)
print(client.zcard('zset'))

client.