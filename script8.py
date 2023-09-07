import multiprocessing
import psutil
import os
import time

from utils import get_data


def worker(i):
    current_process = psutil.Process()
    print(f"Memory consumption at the start {current_process.memory_info().rss / 1024 ** 2} MB")

    df = get_data(i)
    sum_df = df.groupby(by=df.columns).sum()

    print(f"Memory consumption at the end {current_process.memory_info().rss / 1024 ** 2} MB")

    return sum_df


if __name__ == '__main__':
    multiprocessing.set_start_method("fork")

    start = time.time()

    results = []

    with multiprocessing.Pool(processes=5) as pool:
        for i in range(3):
            results.extend(pool.map(worker, [i for i in range(os.cpu_count())]))

    print(f"Time taken: {time.time() - start}")
    print(len(results))
