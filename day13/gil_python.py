#The GIL (Global Interpreter Lock) is a mutex that protects access to Python objects, preventing multiple threads from executing Python bytecode simultaneously. 

# One thread runs at a time — even on multi-core CPUs, only one thread executes Python code at any given moment.
# It exists in CPython (the standard Python implementation). Other implementations like Jython or IronPython don't have a GIL.
# It simplifies memory management — CPython uses reference counting for garbage collection, and the GIL prevents race conditions on object reference counts.

#The GIL makes single-threaded Python fast and memory-safe, but it's a bottleneck for multi-threaded CPU-bound programs. It's not a bug to fix — it's a design trade-off in CPython. For true CPU parallelism, use processes or C extensions that release the GIL.

#Thread Pool Executor (I/O Bound)
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests

urls = ["https://example.com"] * 20

def fetch(url):
    return requests.get(url, timeout=10).status_code

with ThreadPoolExecutor(max_workers=10) as executor:
    futures = {executor.submit(fetch, url): url for url in urls}
    
    for future in as_completed(futures):
        url = futures[future]
        try:
            status = future.result()
            print(f"{url}: {status}")
        except Exception as e:
            print(f"{url}: {e}")

#Each thread releases the GIL while waiting for the network response, so others can run.

#Process Pool Executor (CPU Bound)
from concurrent.futures import ProcessPoolExecutor
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

if __name__=="__main__":

    numbers = [112_272_535_095_293, 115_280_095_190_773, 109_972_689_928_5419]
    with ProcessPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(is_prime, numbers))
        print(results)
#Each process has its own Python interpreter and GIL, so they run on separate CPU cores in parallel.

#The Modern Way
# from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# def run_io_tasks(tasks):
#     with ThreadPoolExecutor() as executor:
#         return list(executor.map(task_func, tasks))

# def run_cpu_tasks(tasks):
#     with ProcessPoolExecutor() as executor:
#         return list(executor.map(task_func, tasks))
