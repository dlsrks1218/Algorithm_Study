import time

def time_format(t):
    return time.strptime(t, '%Y-%m-%d %H:%M:%S')[0:6]

if __name__ == '__main__':
    timestamp = [
        '2018-12-12 01:17:31',
        '2018-12-12 01:17:48',
        '2018-12-12 01:19:12',
        '2018-12-12 01:07:21',
        '2018-12-12 02:47:33',
        '2018-12-12 02:17:51',
        '2018-12-12 01:15:31'
    ]
    # 최신 순 정렬
    timestamp.sort(key=time_format, reverse=True)
    for ts in timestamp:
        print(ts)
    print()
    # 시간 순 정렬
    timestamp.sort(key=time_format, reverse=False)
    for ts in timestamp:
        print(ts)