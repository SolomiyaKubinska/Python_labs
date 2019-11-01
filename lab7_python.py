from urllib import request

def download_file(url):
    file = request.urlopen(url)
    file_text = str(file.read()).split("\\n")

    new_file = open("file.txt", "w")
    for text in file_text:
        new_file.write(text + "\n")
    new_file.close()
    return new_file.name

def count_stats(file):
    dictionary = {}
    with open(file) as f:
        for line in f:
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
