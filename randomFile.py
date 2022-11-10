import sys

import win32com
from win32com.client import gencache


def get_file_metadata(path, filename, metadata):
    # Path shouldn't end with backslash, i.e. "E:\Images\Paris"
    # filename must include extension, i.e. "PID manual.pdf"
    # Returns dictionary containing all file metadata.
    sh = win32com.client.gencache.EnsureDispatch('Shell.Application', 0)

    print('path: ', path)
    ns = sh.NameSpace(0)
    print('sh: ', sh)
    print('namespace: ', ns)

    # Enumeration is necessary because ns.GetDetailsOf only accepts an integer as 2nd argument
    file_metadata = dict()

    item = ns.ParseName(filename)
    for ind, attribute in enumerate(metadata):
        attr_value = ns.GetDetailsOf(item, ind)
        ns.Set
        if attr_value:
            file_metadata[attribute] = attr_value

    return file_metadata


# *Note: you must know the total path to the file.*
# Example usage:
if __name__ == '__main__':
    print(sys.platform)
    folder = 'C:/Users/Gleb/PycharmProjects/metaData/input_imgs'
    filename = 'usualpng.png'
    # metadata = ['Name', 'Size', 'Item type', 'Date modified', 'Date created']
    metadata = ['Name', 'Size', 'Item type', 'Date modified', 'Date created', 'Date accessed', 'Attributes',
                'Offline status', 'Availability', 'Perceived type', 'Owner', 'Kind', 'Date taken',
                'Contributing artists', 'Album', 'Year', 'Genre', 'Conductors', 'Tags', 'Rating', 'Authors', 'Title',
                'Subject', 'Categories', 'Comments', 'Copyright', '#', 'Length', 'Bit rate', 'Protected',
                'Camera model', 'Dimensions', 'Camera maker', 'Company', 'File description', 'Masters keywords',
                'Masters keywords']
    print(get_file_metadata(folder, filename, metadata))
