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


    