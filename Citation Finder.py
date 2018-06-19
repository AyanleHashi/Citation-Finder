from codecs import decode
import scholarly
import subprocess
import ftfy

search_query = scholarly.search_pubs_query('Maintaining and Operating a Public Information Repository')
pub = next(search_query)

titles = []
for citation in pub.get_citedby():
    titles.append(citation.bib["title"])

text = ""
for title in titles:
    command = "scholar.py -c 1 --phrase \"{}\" --citation en".format(title)
    process = subprocess.Popen(command,stdout=subprocess.PIPE,shell=True)

    out = process.communicate()[0].decode("utf-8").replace(r"\r","")[2:-7]
    out = decode(out,"unicode_escape")
    
    if "Journal Article" in out or "Conference Proceedings" in out:
        text += out + "\n\n"

with open("endnote.enw","w",encoding="utf-8") as f:
    f.write(ftfy.fix_text(text))
