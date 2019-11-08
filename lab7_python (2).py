from urllib import request

def download_file(url):
    file = request.urlopen(url)
    CHUNK = 1024 * 512
    while 1:
        file_text = str(file.read(CHUNK)).split("\\n")
        if not file_text:
            break
        return file_text

def count_stats(file):
    dictionary = {}
    for line in file:
        line = line.strip().lower()
        words = line.split(' ')
        for word in words:
            if word in dictionary:
                dictionary[word] += 1
            else:
                dictionary[word] = 1
    for word in dictionary.keys():
        print(f"{word} : {dictionary[word]}")
    return dictionary

def words_count(dictionary):
    s = 0
    for word in dictionary.keys():
        s += dictionary[word]
    return s


def main():
    url = input("Enter the url file: ")
    file = download_file(url)
    print("Statistics of words in file: ")
    count_stats(file)
    print(f"Amount of words - {words_count(count_stats(file))}")


if __name__ == '__main__':
    main()
