class FileIO:
    def __init__(self, file_name, open_mode = 'r'):
        self.file_name = file_name
        self.open_mode = open_mode.lower()[0]
        try:
            self.file = open(file_name, self.open_mode)
        except:
            pass

    def read_from(self):
        try:
            return self.file.readlines()
        except:
            return 'Error Occured'

    def write_to(self):
        try:
            write = input('What do you want to put? ')
            self.file.write(write)
            return 'Success'
        except:
            return 'Error'

    def perform_operation(self):
        if 'r' in self.open_mode:
            return  self.read_from()
        elif self.open_mode == 'w' or self.open_mode == 'a':
            return self.write_to()