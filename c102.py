from os import name
import cv2
import dropbox
import time
import random

startTime = time.time()


def take_ss():
    number = random.randint(0, 100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True

    while(result):
        ret, frame = videoCaptureObject.read()
        imageName = "img" + str(number) + ".jpg"
        cv2.imwrite("culprit1.jpg", frame)
        startTime = time.time()
        result = False

    return imageName
    print("snap taken!")

    videoCaptureObject.release()
    cv2.destroyAllWindows()


def upload_file(imageName):
    access_token = 'Bq3gUrCdCVEAAAAAAAAAAUDRg4awYVxZgfqWmPIRxESrUfDmj3TpeqZ6yhYqNQEL'
    file_from = imageName
    file_to = '/c102/' + (imageName)
    """upload a file to Dropbox using API v2
        """
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to,
                         mode=dropbox.files.WriteMode.overwrite)


def main():
    while(True):
        if((time.time() - startTime) >= 10):
            name = take_ss()
            upload_file(name)


main()
