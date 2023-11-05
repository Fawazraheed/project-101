import dropbox 
class Transfer_data:
    def __init__ (self,access_token):
        self.access_token=access_token 
    def upload_file (self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        for root,dirs,files in os.walk(file_from):
            for file_name in files:
                local_path=os.path.join (root,file_name)
                relative_path=os.path.relpath (local,file_from):
                dropbox_path=os.path.join(file_to,relative_path)
                with open(local_path,'rb') as f:
                    dbx.files_upload (f.read(),dropbox_path,mode=WriteMode('overwrite'))
def main():
    access_token= 'sl.BnjQq3FP5YwnTRZb7vR67YwvCDYY-3Ii8i8ZO_z2jm_l3TmjpMSBwZQ7xeFi6lI-PULW7x4Wu3YE1LPHTap8jT-G8CqwHnKGihet0BL5XGrwB3YRxbRz8s8Y3h2M8CTGVVbBKnYx7auV'
    transferData = TransferData(access_token) 
    file_from= 'Downloads/unredacter-main' 
    file_to= 
     