from bs4 import BeautifulSoup
import requests
import subprocess

title = "BIOMEDICAL IMAGE RETRIEVAL USING LBWP"
"""title = title.replace(" ","+")
site = "https://www.ncbi.nlm.nih.gov/pubmed/?term="

soup = BeautifulSoup(requests.get(site+title).text,"lxml")
try:
    for tag in soup.find_all("dd"):
        try:
            doi = tag.a.text
        except IndexError:
            pass
except IndexError:
    print("Article doesn't appear on PubMed")
except AttributeError:
    print("More than one search result returned")

print(doi)"""

command = "scholar.py -c 1 --phrase \"{}\"".format(title)
process = subprocess.Popen(command,stdout=subprocess.PIPE,shell=True)
out = process.communicate()[0].decode("cp1252").replace(r"\r","")
url = out[out.find("URL")+4:out.find("Year")][:-12]

if "scholar" in url:
    url = url[26:]

print(url)