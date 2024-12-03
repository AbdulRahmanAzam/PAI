import nltk
nltk.download('punkt_tab', force = True)
nltk.download('wordnet', force=True)
nltk.download('averaged_perceptron_tagger_eng', force=True)
from nltk.tokenize import word_tokenize, sent_tokenize

from nltk.corpus import stopwords

from nltk.stem import PorterStemmer, WordNetLemmatizer

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

paragraph = "This is a simple sentence. Tokenize for me, 'Please'."


### TOKENIZATION
tokenize_sentences = sent_tokenize(paragraph)
print("tokenize sentence",tokenize_sentences)

tokenize_words = word_tokenize(paragraph)
print("Tokenize words: ", tokenize_words)

tokenize_characters = list(paragraph)
print("tokenize characters",tokenize_characters)


### STEMMING
stemmer = PorterStemmer()
# for i in range(len(tokenize_sentences)):
#     words = nltk.word_tokenize(tokenize_sentences[i])
#     words = [stemmer.stem(word) for word in words if word not in set(stopwords.words('english'))]
#     tokenize_sentences[i] = ' '.join(words)
# OR
tokenize_sentences = [' '.join(stemmer.stem(word) for word in word_tokenize(sentence) if word not in set(stopwords.words("english"))) for sentence in tokenize_sentences]
print("Stemming: " ,tokenize_sentences)

### LEMMATIZATION
lemmatizer = WordNetLemmatizer()
# for i in range(len(tokenize_sentences)):
#     words = nltk.word_tokenize(tokenize_sentences[i])
#     words = [lemmatizer.lemmatize(word) for word in words if word not in set(stopwords.words("english"))]
#     tokenize_sentences[i] = ' '.join(words)
# OR
tokenize_sentences = [' '.join(lemmatizer.lemmatize(word) for word in word_tokenize(sentence) if word not in set(stopwords.words("english"))) for sentence in tokenize_sentences]
print("Lemmatization: ", tokenize_sentences)

### POS TAGGING
from nltk import pos_tag
sentence_tag = "Stemming helps in preprocessing text."
tokens = word_tokenize(sentence_tag)
pos_tags = pos_tag(tokens)
print("Pos tags",pos_tags)


### COUNT VECTORIZER
count_vectorizer = CountVectorizer()
count_vectors = count_vectorizer.fit_transform(tokenize_sentences)

print("Count Vectorizer Vocablulary: \n", count_vectorizer.get_feature_names_out())
print("Count Vectorizer Matrix: \n", count_vectors.toarray())


### TF-IDF VECTORIZER
tfidf_Vectorizer = TfidfVectorizer()
tfidf_vector = tfidf_Vectorizer.fit_transform(tokenize_sentences)

print("TF-IDF vocabulary: \n", tfidf_Vectorizer.get_feature_names_out())
print("Tf-idf Matrix: \n", tfidf_vector.toarray())
