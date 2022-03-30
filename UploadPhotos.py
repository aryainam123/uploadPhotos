import dropbox
import os
import shutil
import time

start_time = time.time()

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)
def main():
    access_token = 'sl.BD-3K0-CPRbjWTKb0i6GtC7aJbI7A5_nEErNch5er81mROLhkbTa6PXgsKT729veVvNHjFhh5CKkxHbe3ZUwLB420FRShKkZsvD-ATakHIiadtw3BzXZ55X_QoXbTaUNxGxF0Fs'
    transfer_data = TransferData(access_token)
    file_from = "img2.png"
    file_to = "/Photos/"+file_from
    if(time.time()-start_time>=172800):
        transfer_data.upload_file(file_from,file_to)
    
main()