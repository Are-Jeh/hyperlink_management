from gensim import corpora, models
from general import *
from gensim import similarities
#from gensim import models
#algo lda a=1, lsi and then tfidf
def LDAmodel(setofdocs , query ,dictionary, document_tm):

    texts = cleandata(setofdocs)
    #dictionary,dtm=create_corpus(texts)
    # generate LDA model
    lda = models.ldamodel.LdaModel(dtm, num_topics=50, id2word = dictionary, passes=20)
    #index.save("simIndex.index")

    vec_bow = dictionary.doc2bow(query)
    vec_lda = lda[vec_bow]
    index = similarities.MatrixSimilarity(lda[dtm])
    sims = index[vec_lda]
    #sims = sorted(enumerate(sims), key=lambda item: -item[1])
    return sims

def jensen_shannon(query , matrix):
    """
    This function implements a Jensen-Shannon similarity
    between the input query (an LDA topic distribution for a document)
    and the entire corpus of topic distributions.
    It returns an array of length M where M is the number of documents in the corpus
    """
    # lets keep with the p,q notation above
    p = query[None,:].T # take transpose
    q = matrix.T # transpose matrix
    m = 0.5*(p + q)
    return np.sqrt(0.5*(entropy(p,m) + entropy(q,m)))


