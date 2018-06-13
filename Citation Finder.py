from codecs import decode
import scholarly
import subprocess

search_query = scholarly.search_pubs_query('Maintaining and Operating a Public Information Repository')
pub = next(search_query)

IDs = []
for citation in pub.get_citedby():
    try:
        IDs.append(str(citation.id_scholarcitedby))
    except AttributeError:
        pass

text = ""
for i in IDs:
    command = "scholar.py -C {} --citation en".format(i)

    process = subprocess.Popen(command,stdout=subprocess.PIPE,shell=True)

    out = process.communicate()[0].decode("utf-8").replace(r"\r","")[2:-7]
    out = decode(out,"unicode_escape")

    text += out + "\n\n"

with open("endnote mini.enw","w",encoding="utf-8") as f:
    f.write(text)
