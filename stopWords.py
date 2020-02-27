import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
  
example_sent = "К общим можно отнести предлоги, суффиксы, причастия, междометия, цифры, частицы и т. п. Общие шумовые слова всегда исключаются из поискового запроса (за исключением поиска по строгому соответствию поисковой фразы), также они игнорируются при построении инвертированного индекса. Считается, что каждое из общих стоп-слов есть почти во всех документах коллекции. Зависимые стоп-слова зависят от поисковой фразы. Идея заключается в том, чтобы по-разному учитывать отсутствие просто слов из запроса и зависимых стоп-слов из запроса в найденном документе."

#stopwords = nltk.download('stopwords')
stop_words = set(stopwords.words('english')) 
  
word_tokens = word_tokenize(example_sent) 
  
filtered_sentence = [w for w in word_tokens if not w in stop_words] 
  
filtered_sentence = [] 
  
for w in word_tokens: 
    if w not in stop_words: 
        filtered_sentence.append(w) 
  
print(word_tokens) 
print(filtered_sentence) 