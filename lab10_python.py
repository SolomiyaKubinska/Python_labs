import os
from urllib import request
from threading import Thread

class download_file_1(Thread):
    def __init__(self, url, num):
        Thread.__init__(self)
        self.num = num
        self.url = url

    def run(self):
        file = request.urlopen(self.url)
        path = os.path.basename(self.url)
        with open(path, "wb") as f:
            CHUNK = 1024 * 512
            while True:
                file_text = file.read(CHUNK)
                if not file_text:
                    break
                f.write(file_text)
        result = f"{self.num}. {self.url} is downloaded!"
        print(result)

class download_file_2(Thread):
    def __init__(self, url, num):
        Thread.__init__(self)
        self.num = num
        self.url = url

    def run(self):
        file = request.urlopen(self.url)
        path = os.path.basename(self.url)
        with open(path, "wb") as f:
            CHUNK = 1024 * 512
            while True:
                file_text = file.read(CHUNK)
                if not file_text:
                    break
                f.write(file_text)
        result = f"{self.num}. {self.url} is downloaded!"
        print(result)

def main(urls0):
    thread_1 = download_file_1(urls0, 1)
    thread_1.start()
    thread_2 = download_file_2(urls0, 2)
    thread_2.start()


if __name__ == "__main__":
    urls = str(input("Enter url file: "))
    main(urls)
