from gensim import models
from general import *
from gensim import similarities
def LSImodel( clean_content , query, dictionary, document_tm ) :

    #dictionary , document_tm = create_corpus(clean_content)
    #dictionary.save_as_text('deerwester_text.dict')

    lsi = models.LsiModel(document_tm, id2word=dictionary, num_topics=15)
    vec_bow = dictionary.doc2bow(query)
    vec_lsi = lsi[vec_bow]  # convert the query to LSI space
    #print(vec_lsi)


    index = similarities.MatrixSimilarity(lsi[document_tm])  # transform corpus to LSI space and index it
    #index.save('dictionary.index')
    #index = similarities.MatrixSimilarity.load('dictionary.index')
    #print(index)

    sims = index[vec_lsi]  # perform a similarity query against the corpus
    #print(sims)
    return sims


