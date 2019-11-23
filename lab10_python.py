import os
from urllib import request
from threading import Thread

class download_file(Thread):
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
    for num, url in enumerate(urls0):
        thread = download_file(url, num+1)
        thread.start()


if __name__ == "__main__":
    urls = input("Enter some url files: ").split(' ')
    main(urls)
