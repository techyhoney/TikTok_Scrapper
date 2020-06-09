from TikTokApi import *
import time, sys, os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

import zipfile

def zipdir(path, ziph):
    # Fucntion to Zip the folder
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))

def gdrive_upload(str):
	g_login = GoogleAuth()
	g_login.LocalWebserverAuth()
	drive = GoogleDrive(g_login)
	file2 = drive.CreateFile()
	file2.SetContentFile(str)
	file2.Upload()

api = TikTokApi()

results = 1900
vid=""
username=""
trending=""
if(sys.argv[1]=="u"):
	username=sys.argv[2]
	trending = api.byUsername(username,results)
elif(sys.argv[1]=="h"):
	username=sys.argv[2]
	trending = api.byHashtag(username,results)

if(not os.path.exists(username)): 
	os.mkdir(username)
videoname="_video.mp4"
count=0
for tiktok in trending:
    # Prints the text of the tiktok
    count=count+1
    if count%10==0:
    	print("Please wait for 5 sec to continue....")
    	time.sleep(5)
    if(sys.argv[1]=="u"):
    	vid=tiktok['id']
    elif(sys.argv[1]=="h"):
    	vid=tiktok['itemInfos']['id']
    url='https://www.tiktok.com/@'+username+'/video/'+vid+'?lang=en'
    print("Downloaded: " + str(count))
    # Below is used if you want no watermarks
    tiktokData = api.get_Video_No_Watermark(url,return_bytes=1)
    with open(username+"/"+vid+"_"+username+videoname,'wb') as out:
    	out.write(tiktokData)

#print(api.getUserObject(username))
print(len(trending))
zipf = zipfile.ZipFile(username + '.zip', 'w', zipfile.ZIP_DEFLATED)
zipdir(username+"/", zipf)
zipf.close()
gdrive_upload(username + '.zip')
