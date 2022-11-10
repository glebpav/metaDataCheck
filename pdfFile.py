from pdfrw import PdfReader, PdfWriter

file_path = "input_imgs/my_pdf_example.pdf"
clear_path = "clear_imgs/my_pdf.pdf"

"""

trailer = PdfReader(file_path)
trailer.Info.Owner = "New name"
PdfWriter(clear_path + "/edited.pdf", trailer=trailer).write()"""

"""from pyPdf import PdfFileWriter, PdfFileReader
from pyPdf.generic import NameObject, createStringObject

OUTPUT = 'output.pdf'
INPUTS = ['test1.pdf', 'test2.pdf', 'test3.pdf']

# There is no interface through pyPDF with which to set this other then getting
# your hands dirty like so:
infoDict = output._info.getObject()
infoDict.update({
    NameObject('/Title'): createStringObject(u'title'),
    NameObject('/Author'): createStringObject(u'author'),
    NameObject('/Subject'): createStringObject(u'subject'),
    NameObject('/Creator'): createStringObject(u'a script')
})

inputs = [PdfFileReader(i) for i in INPUTS]
for input in inputs:
    for page in range(input.getNumPages()):
        output.addPage(input.getPage(page))

outputStream = file(OUTPUT, 'wb')
output.write(outputStream)
outputStream.close()
"""


from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader(file_path)
writer = PdfWriter()

# Add all pages to the writer
for page in reader.pages:
    writer.add_page(page)

# Add the metadata
writer.add_metadata(
    {
        "/Author": "Martin",
        "/Producer": "Libre Writer",
    }
)

# Save the new PDF to a file
with open(clear_path, "wb") as f:
    writer.write(f)


reader = PdfReader(clear_path)

meta = reader.metadata

print(len(reader.pages))

# All of the following could be None!
print(meta.author)
print(meta.creator)
print(meta.producer)
print(meta.subject)
print(meta.title)