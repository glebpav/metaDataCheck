import docx

input_dir = "input_imgs/"
output_dir = "clear_imgs/"
# file_name = "someDoc.docx" # works
# file_name = "someDoc.doc" # doesn't work
# file_name = "table.xlsx" # doesn't work

file_name = "my_pdf_example.pdf"

document = docx.Document(input_dir + file_name)
core_properties = document.core_properties
print(core_properties.author)
core_properties.author = "not Gleb2"

document.save(output_dir + file_name)