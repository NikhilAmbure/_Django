import time
import threading

from helper import doSomething
start = time.perf_counter()


if __name__ == "__main__":

    # Using thread => Takes 1 second (Multi-Threading)
    print(f"Thread name is {threading.current_thread().name} with id - {threading.get_ident()}")
    
    names = ["Nikhil", "Parle", "Jonas", "Patti"]

    threads = []
    for name in names:
        thread = threading.Thread(target=doSomething, args=[name])
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()


    finish = time.perf_counter()
    print(f"\nFinished In {round(finish - start, 2)}")