import redis

client = redis.Redis(host='10.0.0.128',password='qwe123')

counts = 'video_counts'
# 清空统计
client.delete(counts)


def counter(video_id: int):
    count_number = client.hget(counts, video_id)
    if count_number:
        count_number = int(count_number) + 1
    else:
        count_number = 1
    
    client.hset(counts, video_id, count_number)
    return count_number


if __name__ == '__main__':
    print('1001 count: {}'.format(counter(1001)))
    print('1001 count: {}'.format(counter(1001)))
    print('1002 count: {}'.format(counter(1002)))
    print('1001 count: {}'.format(counter(1001)))
    print('1001 count: {}'.format(counter(1001)))
    print('1002 count: {}'.format(counter(1002)))


