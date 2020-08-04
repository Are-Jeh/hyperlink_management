from bs4 import BeautifulSoup
import requests
from textanal import *
from lsi import *


website_c=requests.get('http://home.iitj.ac.in/~mkumar/').text
print("website read")
soup = BeautifulSoup(website_c,features="html5lib")
for script in soup(["script", "style"]):
    script.decompose()
source_contents =(soup.get_text()).split()
#source_contents =cleandata(soup.get_text()) #query document
#print(doc)
print("got contents on hand")
h1 = open("hyperlinks.txt","w+")
h = []
f1 = open("faulty.txt" ,"w+")
f = []
#html_content = requests.get(http://home.iitj.ac.in/~mkumar/).text

for link in soup.find_all('a'):
    #print(link.get('href')
    if link.get('href') is not None :
        if link.get('href').startswith('#'):
            continue
        try:
            request = requests.get(link.get('href'))
            if request.status_code == 200 :
                h1.write(link.get('href'))
                h1.write("\n")
                h.append(link.get('href'))
            else :
                f1.write(link.get('href'))
                f1.write("\n")
                f.append(link.get('href'))
        except IOError:
            #print(link.get('href'))
            #print("Not a real URL")
                f1.write(link.get('href'))
                f1.write("\n")
                f.append(link.get('href'))
##########################################
print("found all hyperlinks")
file = open('hyp_con.txt', 'w+')
contents = []
print("file opened")
for line in h :
    hyperlink_string = requests.get(line).text
    soup = BeautifulSoup(hyperlink_string,features="html5lib")
    for script in soup(["script", "style"]):
        script.decompose()    # rip it out
    c=soup.get_text()
    c=c.replace("\n"," ").replace("  "," ")
    contents.append(c)
print("scrapped content")
for content in contents :
    file.write(content)
file.close()
print("scrapped content to file")

#sims = LSImodel(contents , source_contents)
#sims = LDA(contents ,doc)
#for i,hs,sim in enumerate(sims,h, start=1):
#    print(i,hs,sim)

clean_contents = cleandata(contents )
print("cleaned data")
dictionary , dtm = create_corpus(clean_contents)
print("got dick da")
sims = LSImodel(clean_contents ,source_contents , dictionary , dtm )



for a,b in zip(h,sims) :
    print(a , b)
print('###############################################################')
#array = jensen_shannon(source_contents,dtm)
#print(array)
f1.close()
h1.close()
'''
print('Comparing Result:', sims[query_doc_tf_idf])

f1.close()
h1.close()

tf_idf = gensim.models.TfidfModel(corpus)
for doc in tfidf[corpus]:
    print([[dictionary[id], np.around(freq, decimals=2)] for id, freq in doc])
building index
sims = gensim.similarities.Similarity('workdir/',tf_idf[corpus],
                                        num_features=len(dictionary))
'''
