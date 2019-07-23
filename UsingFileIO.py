from FileIOClass import FileIO

name = input('What file do you want to open? ')
openmode = input('How do you want to open the file? (Read/Write/Append etc.) ')

my_file = FileIO(name, openmode)
