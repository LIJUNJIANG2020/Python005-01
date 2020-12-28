import redis


client = redis.Redis(host="10.0.0.128", port=6379, password='qwe123')

client.set('key', 'value')

result = client.get('key')

print(f'get: {result}')

client.append('key', 'add')
print(f'append: {client.get("key")}')
# ÎÎÎ
client.set('key2', 100)

res = client.incr('key2')
print(f'incr: {res}')

res = client.decr('key2')
print(f'derc: {res}')
