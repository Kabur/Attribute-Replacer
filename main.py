import os
import taglib # HOW TO INSTALL TAGLIB FOR PYTHON: https://github.com/supermihi/pytaglib
# todo: only works on mp3's so far, didn't test for others


def replace(path, artist, album, title, level, recursive=True):
    for item in os.listdir(path):
        # if it's an mp3
        if os.path.isfile(path + item):
            if item.split('.')[-1] != 'mp3':
                continue
            file = taglib.File(path + item)

            if artist == 'delete':
                del file.tags['ARTIST']
            elif artist != '':
                file.tags['ARTIST'] = [artist]

            if album == 'delete':
                del file.tags['ALBUM']
            elif album != '':
                file.tags['ALBUM'] = [album]
            else:
                file.tags['ALBUM'] = [path.split("\\")[-2]]
                # if level == 0:
                #     file.tags['ALBUM'] = [path.split("\\")[-2]]
                # elif level == 1:
                #     file.tags['ALBUM'] = [path.split("\\")[-3] + ": " + path.split("\\")[-2]]


            if title == 'delete':
                del file.tags['TITLE']
            elif title != '':
                file.tags['TITLE'] = [title]
            else:
                file.tags['TITLE'] = [item]

            return_value = file.save()
            if return_value:
                print("Some attributes could not be saved: ")
                print(return_value)

        # if its a directory
        elif os.path.isdir(path + item):
            if recursive:
                print("Diving into: " + item)
                replace(path + item + '\\', artist, album, title, level + 1, True)
            else:
                print("Skipping a folder: " + path + item)
        else:
            print("Found not a folder, neither a file, skipping: " + path + item)


if __name__ == '__main__':
    root_folder = input("Type the root folder path: ")
    recursive = input("Run for each subfolder too? y/n: ")
    if recursive == 'y':
        recursive = True
    # root_folder = 'E:\Dropbox\Python\Attribute-Replacer\\test_dir'
    album = input("Replace the 'Album' attribute with the given text \n"
                  "OR leave empty to replace with the respective folder name \n"
                  "OR type 'delete' to remove all albums\n"
                  "Album name: ")
    artist = input("Replace the 'Contributing Artists' attribute with the given text \n"
                   "OR leave empty for not replacing \n"
                   "OR type 'delete' to remove all artists \n"
                   "Artist name: ")
    title = input("Replace the 'Title' attribute with the given text \n"
                  "OR leave empty to replace with the respective filenames \n"
                  "OR type 'delete' to remove all titles \n"
                  "Title: ")

    replace(root_folder + '\\', artist, album, title, -1, recursive)


'''
import win32api
import win32con

file = 'test'
f = open('test', 'w')
f.close()

make the file hidden
win32api.SetFileAttributes(file, win32con.FILE_ATTRIBUTE_HIDDEN)

make the file read only
win32api.SetFileAttributes(file, win32con.FILE_ATTRIBUTE_READONLY)

to force deletion of a file set it to normal
win32api.SetFileAttributes(file, win32con.FILE_ATTRIBUTE_NORMAL)
os.remove(file)
'''
