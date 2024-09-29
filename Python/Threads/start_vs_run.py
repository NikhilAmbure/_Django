# "start" creates multiple threads. 
# while "run" can work on single thread. So, 
# it will work on same id thread and no need to use "join" here

import time
import threading

from threads_with_class import DoSomething
from helper import doSomething
start = time.perf_counter()


if __name__ == "__main__":

    # Using thread => Takes 1 second (Multi-Threading)
    print(f"Thread name is {threading.current_thread().name} with id - {threading.get_ident()}")
    
    # names = ["Nikhil", "Parle", "Jonas", "Patti"]

    # threads = []
    # for name in names:
    #     thread = threading.Thread(target=doSomething, args=[name])
    #     thread.run()
    #     threads.append(thread)


    # threads with class

    t1 = DoSomething()
    t1.start()
    t2 = DoSomething()
    t2.start()
    t1.join()
    t2.join()

    finish = time.perf_counter()
    print(f"\nFinished In {round(finish - start, 2)}")