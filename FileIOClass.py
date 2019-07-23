class FileIO:
    def __init__(self, file_name, open_mode = 'r'):
        self.file_name = file_name

        self.open_mode = open_mode
        self.file = open(file_name, open_mode)
        if self.open_mode == 'r':
            self.readfrom()
        elif self.open_mode == 'w':
            self.writeto()

    def readfrom(self):
        try:
            return self.file.readlines()
        except:
            return 'Error Occured'

    def writeto(self):
        try:
            write = input('What do you want to put? ')
            self.file.write(write)
            return 'Success'
        except:
            return 'Error'
