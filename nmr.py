#file functions
import os
#time functions
from datetime import datetime

#TODO
#redo function to use date and time format


#print day in day/month/year format
dateTest = datetime.now().strftime("%#m/%d/%y")
#print time in hour:minuteAM/PM format
timeTest = datetime.now().strftime("%#I:%M%p")
formatTest = dateTest + " at " + timeTest 
print(formatTest)

#main rename function 
def rename_files(directory, newname):
    files = os.listdir(directory)
    counter = 1
    for file in files:
        #split on '.' and grab last element to keep extension type
        filetype = file.split(".")[-1]
        #rename takes two args, (folder + filename, folder + newname)
        os.rename(directory + "/" + file, directory + "/" + newname + str(counter) + "." + filetype)
        counter += 1
        #test
        print("renamed file " + file + "to " + newname + str(counter) + "." + filetype)

path = R"C:\Users\zvd19\source\temp\testdir"

rename_files(path, "works")