"""
In this programe we are using to check the unique words we want and to say how many time the word has occured
As a further motive if I am given a text file and I want to find some important keywords in the document I will search
for that word.
"""
import re
from collections import Counter

def count_words(file_path):
    with open(file_path, encoding= 'utf-8') as file:
        all_words= re.findall(r"[0-9a-zA-Z-']+", file.read())
        print(all_words)
        all_words = [word.upper() for word in all_words]
        print('\n totalwords:', len(all_words))

        word_counts = Counter()
        for word in all_words:
            word_counts[word]+=1

        print('\n Top words')
        for word in word_counts.most_common(100):
            print(word[0],'\t', word[1])


if __name__ == '__main__':
    count_words("Karan - 1st 100 Reruit - IRE .txt")


