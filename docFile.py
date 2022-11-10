import zipfile
from lxml import etree

# open zipfile - a docx file is essentially a zip of XML files
zf = zipfile.ZipFile('input_imgs/someDoc.doc')

# read in the xml metadata from the file
doc = etree.fromstring(zf.read('docProps/core.xml'))

# retrieve 'creator'
ns={'dc': 'http://purl.org/dc/elements/1.1/'}
creator = doc.xpath('//dc:creator', namespaces=ns)[0].text