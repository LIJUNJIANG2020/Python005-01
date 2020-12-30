import redis
# import time


client = redis.Redis(host='10.0.0.128', password='qwe123')


def send_ms(telephone_number: int, content: str):
    count = client.get(telephone_number)
    
    if count is None:
        client.set(telephone_number, 1, ex=60)
        print(f'{telephone_number} 发送1次成功: {content}')
    else:
        if int(count) < 5:
            client.incr(telephone_number)
            count = client.get(telephone_number)
            print(f'{telephone_number} 发送{count.decode()}次成功: {content}')
        else:
            print(f'{telephone_number}: 1 分钟内发送次数超过 5 次, 请等待 1 分钟')


if __name__ == '__main__':
    send_ms(12345654321, content="hello")
    send_ms(12345654321, content="hello")
    send_ms(88887777666, content="hello")
    send_ms(12345654321, content="hello")
    send_ms(12345654321, content="hello")
    send_ms(88887777666, content="hello")
    send_ms(12345654321, content="hello")
    send_ms(12345654321, content="hello")
