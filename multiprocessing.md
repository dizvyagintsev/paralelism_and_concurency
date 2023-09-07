What we have learned about multiprocessing in Python
1. Each process has its own memory space (address space)
2. Starting a process is expensive (starting interpreter, loading modules, serializing objects, etc.)
3. Communication between processes is expensive (pickling, copying, etc.)
4. `if __name__ == '__main__'` is important 
5. Starting a process can be optimized by:
   1. Using `multiprocessing.Pool` to create a pool of processes (no recreation)
   2. Decreasing size of module to be imported
   3. Decreasing size of arguments to be passed
   4. Decreasing size of return values or not returning anything
   5. Using fork instead of spawn (be careful and test it)
6. Processes are independent (one can die without affecting others)
7. Beware race conditions when work with shared resources (shared values, files, etc.)
8. Number of processes is limited by number of CPUs and memory
9. COW, forks and orphans 