import codecs

file = codecs.open("freq_general_ru.txt", "r", "utf-8")
topWords = []
for line in file:
    words = line.split()
    topWords.extend(words)
file.close()

file = codecs.open("stop_words_ru.txt", "r", "utf-8")
stop_words = []
for line in file:
    words = line.split()
    stop_words.extend(words)
file.close()

filtered_sentence = [w for w in topWords if not w in stop_words and w.isalnum() and not w.isdigit()]

print(topWords)
print(filtered_sentence)