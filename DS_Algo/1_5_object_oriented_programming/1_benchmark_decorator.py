'''
벤치마크(benchmark)는 컴퓨팅에서 특정 오브젝트에 대해 일반적으로 수많은 표준 테스트와 시도를 수행함으로써 
오브젝트의 상대적인 성능 측정을 목적으로 컴퓨터 프로그램을 실행하는 행위이다.
'''
import random
import time


def benchmark(func):
    def wrapper(*args, **kwargs):
        t = time.perf_counter()
        res = func(*args, **kwargs)
        print('{0} {1}'.format(func.__name__, time.perf_counter()-t))
        return res
    return wrapper


@benchmark
def random_tree(n):
    temp = [n for n in range(n)]
    for i in range(n+1):
        temp[random.choice(temp)] = random.choice(temp)
    return temp


if __name__ == '__main__':
    random_tree(10000)