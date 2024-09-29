import time
import threading

from helper import doSomething
start = time.perf_counter()


if __name__ == "__main__":

    # Normally we do => Takes 3 seconds
    # doSomething()
    # doSomething()
    # doSomething()

    # finish = time.perf_counter()
    # print(f"Finished in {finish - start} sec")



    # Using thread => Takes 1 second (Multi-Threading)
    print(f"Thread name is {threading.current_thread().name} with id - {threading.get_ident()}")

    
    t1 = threading.Thread(target=doSomething)
    t2 = threading.Thread(target=doSomething)
    t3 = threading.Thread(target=doSomething)

    # start => starts the thread
    t1.start()
    t2.start()
    t3.start()
    # join => before the complete execution of threads the main function i.e this if will wait until the thread execution completion
    t1.join()
    t2.join()
    t3.join()

    finish = time.perf_counter()
    print(f"\nFinished In {finish - start}")