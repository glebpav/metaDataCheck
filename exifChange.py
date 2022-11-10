from exif import Image

folder_path = 'input_imgs'
output_path = 'clear_imgs'
img_filename = 'DSC01041.jpg'
img_path = f'{folder_path}/{img_filename}'

with open(img_path, 'rb') as img_file:
    img = Image(img_file)

print("Is there any exif data: ", img.has_exif)
print("Meta Data: ")

for item in img.list_all():
    print(item, ": ", img.get(item))

print("\nmodify meta data")
print("datetime before", img.get("datetime"))
img['datetime_original'] = '2222:22:22 22:22:22'
img['software'] = "no no no"
img.artist = 'Leonardo di Vinci'
print("datetime after", img.get("datetime"))

# delete data
# img.delete('body_serial_number')

with open(f'{output_path}/{img_filename}', 'wb') as new_image_file:
    new_image_file.write(img.get_file())
