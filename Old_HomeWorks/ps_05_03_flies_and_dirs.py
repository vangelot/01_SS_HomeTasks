
import os

def print_files_and_dirs():
    print('Files and directories amount: ', len(os.listdir()))
    files = 0
    dirs = 0
    for addr in os.listdir():
        if os.path.isdir(addr):
            dirs += 1
            print('| ',addr)
        else:
            print(addr)
            files += 1

    print('Files amonut: ',files,'\nDirectories amount: ',dirs)

print_files_and_dirs()