import cv2
import time
import random
import dropbox
start_time=time.time()

def take_snapshot():
    number=random.randint(0,100)
    #initializing cv2
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        #read the frames while the camera is on
        ret,frame = videoCaptureObject.read()
        image_name="img"+str(number)+".png"
        #cv2.imwrite() method is used to save an image to any storage device
        cv2.imwrite(image_name,frame)
        start_time=time.time
        result = False
    return image_name
    print("snapshottaken")


    # releases the camera
    videoCaptureObject.release()
    #closes all the window that might be opened while this process
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token="FSkMJADFSSMAAAAAAAAAARC7eVT4M_CLK_ZArTJ5V6wN4zB8hww8wQQh4ck-vJq1"
    file=img_name
    file_from=file
    file_to="/folder/"+(img_name)
    dbx=dropbox.Dropbox(access_token)

    with open(file_from,"rb") as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print ("fileuploaded")

def main():
    while(True):
        if((time.time()-start_time)>=5):
            name=take_snapshot()
            upload_file(name)

main()
