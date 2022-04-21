

import urllib.request

from docx import Document
file=urllib.request.urlopen("https://www.163.com/dy/article/G9I64F8805493U4D.html")
read=file.read()
xa=read.decode('utf-8')
document=Document()
paragraph=document.add_paragraph(xa)
document.save("de.docx")




