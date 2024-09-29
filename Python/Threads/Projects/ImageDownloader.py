import time
import threading

from word import ImageDownloader
start = time.perf_counter()

if __name__ == "__main__":

    print(f"Thread name is {threading.current_thread().name} with id - {threading.get_ident()}")

    image_urls = [
    "https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0",
    "https://images.unsplash.com/photo-1557683316-973673baf926",
    "https://images.unsplash.com/photo-1521747116042-5a810fda9664",
    "https://images.unsplash.com/photo-1602524812398-6c72db3af06d",
    "https://images.unsplash.com/photo-1501594907352-04cda38ebc29",
    "https://images.unsplash.com/photo-1494173853739-c21f58b16055"
]


    threads = []
    for url in image_urls:
        thread = ImageDownloader(url)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
    
    finish = time.perf_counter()
    print(f"Finished in {round(finish - start, 2)}")
