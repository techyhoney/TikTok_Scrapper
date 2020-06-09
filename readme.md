
# TikTok API in Python

This is an unofficial api wrapper for TikTok.com in python. With this api you are able to call most trending and fetch specific user information. The user videos will be stored as .zip file and will be automatically uploaded to Google Drive.

## Pre-Requits
1. Python3
2. pip must be installed
3. Google Drive Api must be configured and download json package and name it client_secrets.json

### After Installing these run following commands in terminal:

`1. pip install TikTokApi`
`2. pyppeteer-install`
`3. pip install PyDrive`


### How to Run Script?

1. After running above commands now you need to open terminal in your project folder
   type following command:
   
   **python TikTok.py u tiktok_username**
   
   Ex:  `python TikTok.py u jannat_zubair29` 
	[This will download videos from @jannat_zubair29 TikTok account]
   
2. For Downloading videos by **hashtag** type following command:
   
   **python TikTok.py h hashtag**

   Ex: `python TikTok.py h cat`
       [This will download videos from hastag "cat"]
