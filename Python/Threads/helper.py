import time
import threading

def doSomething(person_name):   
    print(f"Thread name is {threading.current_thread().name} with id - {threading.get_ident()}")
    print(f"Doing Something!! for person {person_name}")
    time.sleep(1)
    print("Done Something")
