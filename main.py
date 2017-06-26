import os
import taglib
# HOW TO INSTALL TAGLIB FOR PYTHON: https://github.com/supermihi/pytaglib

song = taglib.File(".\\audio1.mp3")
print(song.tags)

# import win32api
# import win32con

# file = 'test'
# f = open('test', 'w')
# f.close()

# make the file hidden
# win32api.SetFileAttributes(file, win32con.FILE_ATTRIBUTE_HIDDEN)

# make the file read only
# win32api.SetFileAttributes(file, win32con.FILE_ATTRIBUTE_READONLY)

# to force deletion of a file set it to normal
# win32api.SetFileAttributes(file, win32con.FILE_ATTRIBUTE_NORMAL)
# os.remove(file)
