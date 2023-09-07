import multiprocessing
import os
import time

from utils import get_data


def worker(i):
    df = get_data(i)
    return df.groupby(by=df.columns).sum()


if __name__ == '__main__':
    start = time.time()

    results = []

    with multiprocessing.Pool() as pool:
        for i in range(3):
            results.extend(pool.map(worker, [i for i in range(os.cpu_count() * 2000)]))

    print(f"Time taken: {time.time() - start}")
    print(len(results))
