import gensim

file = gensim.models.word2vec.Text8Corpus('./text8')
model = gensim.models.Word2Vec(file, size=100)
model.save('./text-8_gensim')
