#Tested On Mac (Mojave), Python 2.7
import os, time, fnmatch
#Get User Input
Qest = raw_input("********Python 2.7 File\Folder Search Tool********\nWhat are you searching for ?.\n1.I am Looking for file(Enter 1)\n2.I am Looking for Folders(Enter 2)\n")
#print Qest
#print(len(Qest))
fileCount = 0
folderCount = 0
if int(Qest) is 1:
    filename = raw_input("Enter File name\n")
    for root, dirs, files in os.walk("/"):
        for file in files:
            Res = os.path.relpath(os.path.join(root, file), "/")
            ser =  "*" + filename + ".*"
            #print ser
            if fnmatch.fnmatch(Res.lower(), ser.lower()):
                print Res
                fileCount += 1
    print "Found " + str(fileCount) + " Files"
elif int(Qest) is 2:
    foldername = raw_input("Enter Folder name")
    for root, dirs, files in os.walk("/"):
        for dir in dirs:
            Res = os.path.relpath(os.path.join(root, dir), "/")
            # print os.path.relpath(os.path.join(root, dir), "/")
            if Res.lower().__contains__(foldername.lower()):
                print Res
                folderCount += 1
    print "Found " + str(folderCount) + " Folders"




