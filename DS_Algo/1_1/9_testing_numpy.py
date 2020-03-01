import numpy as np
import time


def trad_version():
    t1 = time.time()
    x = range(10000000)
    y = range(10000000)
    z = []

    for i in range(len(x)):
        z.append(x[i]+y[i])

    return time.time() - t1


def numpy_version():
    t1 = time.time()
    x = np.arange(10000000)
    y = np.arange(10000000)
    z = x + y

    return time.time()- t1


if __name__ == '__main__':
    print(trad_version())
    print(numpy_version())