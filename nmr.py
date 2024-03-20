#file functions
import os
import time

#TODO
#send rename file func to convert button in ui/set file path with select files btn

def rename_files(directory):
    files = os.listdir(directory)
    for file in files:
        #split on '.' and grab ext
        filetype = file.split(".")[-1]
        currentPath = directory + "\\"  + file
        #format name from timestamp
        createTime = os.path.getctime(currentPath)
        timeObj = time.strptime(time.ctime(createTime))
        fTime = time.strftime("%#m-%d-%y, %#I.%M.%S-%p", timeObj)
        os.rename(currentPath, directory + "\\" + fTime + "." + filetype)

# path =(R"C:\Users\MCA\Desktop\testdir")

# rename_files(path)
        
