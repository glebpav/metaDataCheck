import openpyxl

fh = openpyxl.load_workbook("input_imgs/table.xlsx")

obj = fh.properties  # To get old properties
print(obj)  # print old properties

fh.properties.title = "newTitle"  # To set title
fh.properties.category = "newCategory"  # To set category
fh.properties.subject = "newSubject"  # To set subject

##similarly you can set other fields ##

new_obj = fh.properties  # Now get new properties
print(new_obj)  # print new properties

fh.save("clear_imgs/results.xlsx")
