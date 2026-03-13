


#现在不用理解
import csv 
import re


def get_words(filename): #return a list of individual words found in the file
    with open(filename, "r") as f:
        contents = f.read()

    contents = " ".join(contents.split())
    contents = re.sub(r"[^\w\- ]", "", contents)
    contents = re.sub(r"\-\-", " ", contents)
    return contents.split()


def save_counts(counts):
    with open("counts.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(["Word", "Count"])
        for word, count in sorted(counts.items(), key=lambda x: x[1], reverse=True):
            writer.writerow([word, count])


def main():
    '''counts = {}'''
    words = get_words("address.txt")
    lower_counts = [word.lower() for word in words if len(word) > 4]


    '''for word in lower_counts:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1'''
    counts = {word: lower_counts.count(word) for word in lower_counts}
    
    save_counts(counts)

main()