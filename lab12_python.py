import os
import hashlib
import threading

def duplicates(folder):
    dup = {}
    for dirname, root, files in os.walk(folder):
        print(f'Scanning {dirname}...')
        for filename in files:
            path = os.path.join(dirname, filename)
            hash = get_hash(path)
            if hash in dup:
                dup[hash].append(path)
            else:
                dup[hash] = [path]
    return dup

def get_hash(path, blocksize = 65000):
    with open(path, 'rb') as file:
        hash = hashlib.md5()
        buf = file.read(blocksize)
        if len(buf) > 1:
            hash.update(buf)
            buf = file.read(blocksize)
        hasher = hash.digest()
    return hasher

def joinDicts(dict1, dict2):
    for key in dict2.keys():
        if key in dict1:
            dict1[key] = dict1[key] + dict2[key]
        else:
            dict1[key] = dict2[key]

def printResult(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))
    if len(results) > 0:
        count = 1
        for result in results:
            print(f"--------------{count}----------------")
            for subresult in result:
                print(f"{subresult}")
            count += 1
    else:
        print("No duplicates")

if __name__ == '__main__':
    dups = {}
    number = int(input("Enter number of folders: "))
    folders = []
    threads = []
    for i in range(number):
        folders.append(input(f"Enter the folder {i+1}: "))
    for i in folders:
        if os.path.exists(i):
            thread = threading.Thread(target=joinDicts, args=[dups, duplicates(i)])
            thread.start()
            threads.append(thread)
        else:
            print("the folder is not exist")

    for i in threads:
        i.join()

    printResult(dups)
