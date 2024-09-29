import threading
import requests
import uuid


class ImageDownloader(threading.Thread):

    def __init__(self, url):
        self.url = url
        threading.Thread.__init__(self)

    def run(self):
        print(f"Thread name is {threading.current_thread().name} with id - {threading.get_ident()}")
        image = requests.get(self.url).content
        image_name = f"D:\C\Django Course\Python\Threads\Projects\images\ {str(uuid.uuid4())}.jpg"

        with open(image_name, "wb") as image_file:
            image_file.write(image)
            print("Image Downloaded")
