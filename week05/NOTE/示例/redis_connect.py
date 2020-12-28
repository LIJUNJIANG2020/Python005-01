import redis

clinet = redis.Redis(host='10.0.0.128', port=6379, password='qwe123')
print(clinet)
print(clinet.keys())

for key in clinet.keys():
    print(key.decode())