import os

filelist = os.listdir('.')  # get files in current directory
i=1
for filename in filelist:
    if ".gif" in filename:  # only process pictures
        newname = "subject08_" + str(i) + ".gif"
        print(filename + " will be renamed as " + newname)
	i=i+1
        os.rename(filename, newname)
