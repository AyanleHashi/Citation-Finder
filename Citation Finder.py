import scholarly
import subprocess
import codecs
import time
start = time.time()

search_query = scholarly.search_pubs_query('Maintaining and Operating a Public Information Repository')
#search_query = scholarly.search_pubs_query('Lung nodule detection in CT images using deep convolutional neural networks')
pub = next(search_query)

IDs = []
for citation in pub.get_citedby():
    try:
        IDs.append(str(citation.id_scholarcitedby))
    except AttributeError:
        pass

print("Finished getting citations in", time.time() - start, "seconds.")

text = ""
for i in IDs:
    command = "scholar.py -C {} --citation en".format(i)

    process = subprocess.Popen(command,stdout=subprocess.PIPE,shell=True)

    out = process.communicate()[0].decode("utf-8").replace(r"\r","")[2:-7]
    out = codecs.decode(out,"unicode_escape")

    text += out + "\n\n"

with open("endnote.enw","w",encoding="utf-8") as f:
    f.write(text)

print("Total time:", time.time() - start, "seconds.")
