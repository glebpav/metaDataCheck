"""from libxmp import XMPFiles, consts
xmpfile = XMPFiles( file_path="test/samples/BlueSquare.jpg", open_forupdate=True )"""

from PIL import Image

filename = "input_imgs/my_pdf_example.pdf"

""""with Image.open(filename) as im:
    for segment, content in im.applist:
        marker, body = content.split('\x00', 1)
        if segment == 'APP1' and marker == 'http://ns.adobe.com/xap/1.0/':
            # parse the XML string with any method you like
            print(body)"""

"""fd = open(filename)
d = fd.read()
xmp_start = d.find('<x:xmpmeta')
xmp_end = d.find('</x:xmpmeta')
xmp_str = d[xmp_start:xmp_end + 12]
print(xmp_str)"""

from xml.dom.minidom import parse, parseString

# Parse XML from a filename
# document = parse("smiley.svg")
document = parse(filename)

# Parse XML from a file object
with open("smiley.svg") as file:
    document = parse(file)


# Parse XML from a Python string
document = parseString("""\
<svg viewBox="-105 -100 210 270">
  <!-- More content goes here... -->
</svg>
""")
