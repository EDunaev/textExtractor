#!/usr/bin/python
import codecs

file = codecs.open("annot.txt", "r", "utf-8")
allWords = []
uniqWords = []
for line in file:
    words = line.split(" ")
    for word in words:
        allWords.append(word)
    [uniqWords.append(word) for word in words if word not in uniqWords]
file.close()

print("All words: ", len(allWords))
print("Uniq words: ", len(uniqWords))
