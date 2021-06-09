import dropbox
import os
from dropbox.files import WriteMode
import sys


class TransferData:
    def __init__(self, accesstoken):
        self.accesstoken = accesstoken

    def uploadFiles(self, folderPath):
        if(os.path.exists(folderPath)):

            for(root, dirs, files) in os.walk(folderPath):
                for i in files:
                    filepath = os.path.join(folderPath, i)
                    dbx = dropbox.Dropbox(self.accesstoken)
                    filepathOpen = open(filepath, 'rb').read()
                    dropboxPath = "/files/"+i
                    dbx.files_upload(filepathOpen, dropboxPath,
                                     mode=WriteMode('overwrite'))

            print("Congratulations")
            print("Files are uploaded Successfully!")
            print("Thanks For Using My Service")
        else:
            print("Please Enter a Valid Path Of the folder")
            sys.exit(101)

    def uploadAFile(self, filepath):
        if os.path.exists(filepath):
            dbx = dropbox.Dropbox(self.accesstoken)
            filePathOpen = open(filepath, "rb").read()
            if("\\" in filepath):
                splittedFileName = filepath.split('\\')
                dropboxPath = "/only1File/"+splittedFileName[-1]
            else:
                dropboxPath = "/only1File/"+filepath

            dbx.files_upload(filePathOpen, dropboxPath,
                             mode=WriteMode('overwrite'))
            print("Congratulations!")
            print("File Uploaded Sucessfully!")
            print("Thanks For Using My Service")

        else:
            print("Please Enter a Valid Path Of the file")
            sys.exit(101)


folderPathInput = input("Please Enter The Path Of Your Folder\n")
accesstoken = "sl.AyYKhKKoWeA14h6I2QmgLyuZzlX1iYmUpLoYMQNxQKWWmUpDxtXvAqKAcN1di0sObAJAY_RVotwKcytrVpGN7cPG_n09Ka5F13HybUVxUX34AtwGWw5G_I-9TwXvynKO_VN02OE-POTH"
transferData = TransferData(accesstoken)
transferData.uploadFiles(folderPathInput)

optionQuestion = input("Do You Want To Upload A File?\n")

if optionQuestion == "Yeah" or "yeah" or "yes" or "Yes" or "ya" or "Ya" or "yep" or "Yep":

    filePathInput = input("Please Enter the path of your file \n")
    transferData.uploadAFile(filePathInput)
elif optionQuestion == "no" or "No" or "nope" or "Nope":
    print("Thankyou For Using My Service")
    sys.exit(101)


# Made By Swayam Sai Kar
