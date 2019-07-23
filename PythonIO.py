# Python IO or Input Output for file handling
#
# try:
#     file = open('Order.txt', 'a')
# except FileNotFoundError as errmsg:
#     print('Uh oh file not found! ' + str(errmsg))
# except EOFError:
#     print('End of file error!')


def file_reader(file_name):
    try:
        file = open(file_name, 'r')
        for line in file.readlines():
            print(line.replace(' ', '\n'))
        file.close()
    except FileNotFoundError as errmsg:
        print('No File Found', errmsg)
    except ValueError as errmsg:
        print('Something Wrong Happened', errmsg)
    except FileExistsError as errmsg:
        print('File Already Exists', errmsg)

def file_writer(file_name):
    try:
        file = open(file_name, 'w')
        file.write('HI ')
    except FileNotFoundError as errmsg:
        print('No File Found', errmsg)
    except ValueError as errmsg:
        print('Something Wrong Happened', errmsg)
    except FileExistsError as errmsg:
        print('File Already Exists', errmsg)


file_writer('my_file.txt')
file_reader('my_file.txt')


