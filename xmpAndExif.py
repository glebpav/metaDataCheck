import os
import pyexiv2

image_name = "input_imgs/ususalpng.JPG"

metadata = pyexiv2.ImageMetadata(image_name)
metadata.read()
metadata.modified = True
metadata.writable = os.access(image_name, os.W_OK)
metadata['Exif.Image.Copyright'] = pyexiv2.ExifTag('Exif.Image.Copyright', 'copyright@youtext')
metadata.write()
