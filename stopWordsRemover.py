import codecs, re

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

filtered_words_list = [w for w in topWords if not w in stop_words and w.isalnum() and not w.isdigit() and bool(re.search('[а-яА-Я]', w))]

print(len(filtered_words_list))
print(filtered_words_list)

filteredFile = codecs.open("filteredWords.txt", "a", "utf-8")
filteredFile.write("\n".join(filtered_words_list))
filteredFile.close()
