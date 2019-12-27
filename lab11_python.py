import threading

class ReadWriteLock:
    def __init__(self):
        self.__monitor = threading.Lock()
        self.__exclude = threading.Lock()
        self.readers = 0

    def acquire_read(self):
        with self.__monitor:
            self.readers += 1
            if self.readers == 1:
                self.__exclude.acquire()
            self.__exclude.release()

    def release_read(self):
        with self.__monitor:
            self.readers -= 1
            if self.readers == 0:
                self.__exclude.release()
            self.__exclude.release()

    def acquire_write(self):
        self.__exclude.acquire()

    def release_write(self):
        self.__exclude.release()

    def read(self):
        try:
            self.acquire_read()
            yield
        finally:
            self.release_read()

    def write(self):
        try:
            self.acquire_write()
            yield
        finally:
            self.release_write()

def read_lock():
    r = ReadWriteLock()
    with r.read():
        print("Reading")

def write_lock():
    w = ReadWriteLock()
    with w.write():
        print("Writing")

if __name__ == '__main__':
    t1 = threading.Thread(target=read_lock)
    t2 = threading.Thread(target=write_lock)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

