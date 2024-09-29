import threading
import time

from Task_ import NumberPrinter

start = time.perf_counter()

if __name__ == "__main__":
    
    print(f"Thread name is {threading.current_thread().name} with id - {threading.get_ident()}")

    threads = []
    for i in range(1, 101):
        thread = NumberPrinter(i)
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()

    finish = time.perf_counter()
    print(f"Finished in {round(finish - start, 2)}")