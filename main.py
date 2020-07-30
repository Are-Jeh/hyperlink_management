from bs4 import BeautifulSoup
import requests
import csv
#from text import *


#with open("htmldoc.html") as fp:
#    soup = BeautifulSoup(fp,features="html5lib")
html_content = requests.get('http://home.iitj.ac.in/~mkumar/').text
soup = BeautifulSoup(html_content,features="html5lib")
#print(soup.prettify())

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
                #h.write(str(counter))
                #h.write(":")
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
            continue
#f.close()
#h.close()
##########################################
'''
with open('tables.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SN","hyperlink", "hyperlink_text","hyperlink_content","hyperlink_tm"])
file.close()


file = open('hyperlinks.txt', 'r')

while True:
    # Get next line from file
    line = file1.readline()
    # if line is empty
    # end of file is reached
    if not line:
        break
    soup= BeautifulSoup(line.strip(),features="html5lib")
    writer.writerow([counter, line, , soup.get_text()])

file1.close()
'''
file = open('hyp_con.txt', 'w+')
contents = []


for line in h :
    html_content = requests.get(line).text
    soup = BeautifulSoup(html_content,features="html5lib")
    contents.append(soup.get_text().replace("\n"," "))

for content in contents :
    file.write(content)


file.close()



