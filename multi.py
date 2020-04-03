import multiprocessing as mp
import time

def count(name):
    for i in range(1, 100001):
        print(name, " : ", i)


def single(start_time, num_list):
    for num in num_list:
        count(num)
    return time.time() - start_time


def multi(start_time, num_list):
    pool = mp.Pool(mp.cpu_count())
    pool.map(count, num_list)
    pool.close()
    pool.join()
    return time.time() - start_time


if __name__ == '__main__':
    start_time = time.time()
    num_list = ['p1', 'p2', 'p3', 'p4']

    single_result = single(start_time, num_list)
    multi_result = multi(start_time, num_list)

    print(single_result)
    print(multi_result-single_result)