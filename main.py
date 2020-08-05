from bs4 import BeautifulSoup
import requests
from general import *
from lsi import *
print("####################################################################")
print("Hyperlink Management Tool")
print("-this tool will search your webpage and analyse all the hyperlinks\n in them whether they are broken, or redirect to a website\n of a different context-")
print("####################################################################\n")
url_to_analyse = input("Enter URL:")

website_c=requests.get(url_to_analyse).text
print("Reading Website...")
soup = BeautifulSoup(website_c,features="html5lib")
for script in soup(["script", "style"]):
    script.decompose()
source_contents =(soup.get_text()).split()
#source_contents =cleandata(soup.get_text()) #query document
#print(doc)
print("Got contents on hand!")
print("Finding Links...")
hyperlinks_file = open("hyperlinks.txt","w+")
hyperlinks_list = []
faulty_links = open("faulty.txt" ,"w+")
faulty_links_list = []
#html_content = requests.get(http://home.iitj.ac.in/~mkumar/).text

for link in soup.find_all('a'):
    #print(link.get('href')
    if link.get('href') is not None :
        if link.get('href').startswith('#'):
            continue
        try:
            request = requests.get(link.get('href'))
            link_url = link.get('href')
            if request.status_code == 200 :
                if link_url not in hyperlinks_list:
                    hyperlinks_list.append(link_url)
                    hyperlinks_file.write(link_url)
                    hyperlinks_file.write("\n")
            else :
                if link_url not in faulty_links_list:
                    faulty_links.write(link_url)
                    faulty_links.write("\n")
                    faulty_links_list.append(link_url)
        except IOError:
            #print(link.get('href'))
            #print("Not a real URL")
            if link.get('href') not in faulty_links_list:
                faulty_links_list.append(link.get('href'))
                faulty_links.write(link.get('href'))
                faulty_links.write("\n")
##########################################
print("Found all Hyperlinks")
file = open('hyp_con.txt', 'w+')
contents = []
print("File opened")
for line in hyperlinks_list :
    hyperlink_string = requests.get(line).text
    soup = BeautifulSoup(hyperlink_string,features="html5lib")
    for script in soup(["script", "style"]):
        script.decompose()    # rip it out
    c=soup.get_text()
    c=c.replace("\n"," ").replace("  "," ")
    contents.append(c)
print("Scraped content")


for content in contents :
    file.write(content)


file.close()
print("Scraped content to file")


clean_contents = cleandata(contents)
print("Cleaned data")
dictionary , dtm = create_corpus(clean_contents)
print("Received Dictionary")
sims = LSImodel(clean_contents ,source_contents , dictionary , dtm )
print("Printing Results...")


for a,b in zip(hyperlinks_list,sims) :
    print(a , b)
print('###################################################################')
#array = jensen_shannon(source_contents,dtm)
#print(array)
faulty_links.close()
hyperlinks_file.close()
'''
print('Comparing Result:', sims[query_doc_tf_idf])

faulty_links.close()
h1.close()

tf_idf = gensim.models.TfidfModel(corpus)
for doc in tfidf[corpus]:
    print([[dictionary[id], np.around(freq, decimals=2)] for id, freq in doc])
building index
sims = gensim.similarities.Similarity('workdir/',tf_idf[corpus],
                                        num_features=len(dictionary))
'''
