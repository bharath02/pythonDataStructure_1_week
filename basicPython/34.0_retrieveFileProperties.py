# Write a Python program to retrieve file properties.
import os.path
import time
class fileProperties:
    def retrieveFile(self):
        print('File          :',__file__)
        print("Access time   : ",time.ctime(os.path.getatime(__file__)))
        print('Modified time : ', time.ctime(os.path.getmtime(__file__)))
        print('change time   : ',time.ctime(os.path.getctime(__file__)))
        print('Size          : ',os.path.getsize(__file__))
obj=fileProperties()
obj.retrieveFile()