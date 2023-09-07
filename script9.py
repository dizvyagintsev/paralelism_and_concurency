import multiprocessing
import os
import time

from utils import get_data


def worker(i):
    print(i)

    if i == 5:
        raise ValueError("ghjg")

    df = get_data(i)
    sum_df = df.groupby(by=df.columns).sum()

    return sum_df


if __name__ == '__main__':
    start = time.time()

    results = []

    with multiprocessing.Pool() as pool:
        async_results = []
        for i in range(3):
            async_results.extend([pool.apply_async(worker, (i,)) for i in range(os.cpu_count())])

        for async_result in async_results:
            try:
                # results.append(async_result.get())
                pass
            except Exception as e:
                print(f"Error encountered: {e}")

    # time.sleep(10)
    print(f"Time taken: {time.time() - start}")
    print(len(results))
