import os

filelist = os.listdir('.')  # get files in current directory
i=0
for filename in filelist:
    if ".png" in filename:  # only process pictures
        newname = "subject" + str(i) + ".jpg"
        print(filename + " will be renamed as " + newname)
	i=i+1
        os.rename(filename, newname)