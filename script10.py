import multiprocessing
import os
import time

from utils import get_data


def worker(i, lock, counter):
    df = get_data(i)
    result = df.groupby(by=df.columns).sum()

    # Use the lock to safely update the counter
    with lock:
        temp = counter.value + 1
        counter.value = temp
    print(f"Processed {counter.value} tasks")

    return result


if __name__ == '__main__':
    multiprocessing.set_start_method("spawn")

    # Create a manager object
    manager = multiprocessing.Manager()

    # Create shared counter and lock using the manager
    counter = manager.Value('i', 0)
    lock = manager.Lock()

    start = time.time()

    results = []

    with multiprocessing.Pool() as pool:
        for i in range(3):
            # Pass the lock and counter to each worker process
            results.extend(pool.starmap(worker, [(i, lock, counter) for i in range(os.cpu_count())]))

    print(f"Time taken: {time.time() - start}")
    print(len(results))
