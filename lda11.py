from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim
from textanal import * 
#from gensim import similarities


def LDA(setofdocs , doc):

    texts = cleandata(setofdocs)
   
    # turn our tokenized documents into a id <-> term dictionary
    dictionary = corpora.Dictionary(texts)
    # convert tokenized documents into a document-term matrix
    corpus = [dictionary.doc2bow(text) for text in texts]
    # generate LDA model
    lda = gensim.models.ldamodel.LdaModel(corpus, num_topics=50, id2word = dictionary, passes=20)
    #print(ldamodel)
    from gensim import similarities
    #index.save("simIndex.index")

    #docname = "docs/the_doc.txt"
    vec_bow = dictionary.doc2bow(doc.lower().split())
    vec_lda = lda[vec_bow]
    index = similarities.MatrixSimilarity(lda[corpus])
    sims = index[vec_lda]
    #sims = sorted(enumerate(sims), key=lambda item: -item[1])
    return sims
