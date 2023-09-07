import multiprocessing
import time

from utils import get_data


def worker(i, pipe):
    df = get_data(i)
    pipe.send(df.groupby(by=df.columns).sum())
    pipe.close()


if __name__ == '__main__':
    parent_conn1, child_conn1 = multiprocessing.Pipe()
    process1 = multiprocessing.Process(target=worker, args=(1, child_conn1))

    parent_conn2, child_conn2 = multiprocessing.Pipe()
    process2 = multiprocessing.Process(target=worker, args=(2, child_conn2))

    process1.start()
    process2.start()

    print(parent_conn1.recv())
    print(parent_conn2.recv())

    parent_conn1.close()
    parent_conn2.close()

    process1.join()
    process2.join()

