import requests
import xml.etree.ElementTree as ET
import time
apiKey = {Your api key}}

channelID = {Target channel ID}

videos = []

def getLatestVideo(channelID):
    r = requests.get("https://www.youtube.com/feeds/videos.xml?channel_id="+channelID)
    tree = ET.ElementTree(ET.fromstring(r.text))
    root = tree.getroot()
    namespaces = {"yt":"http://www.youtube.com/xml/schemas/2015", "media":"http://search.yahoo.com/mrss/", "xmlns":"http://www.w3.org/2005/Atom"}
    for item in root.findall('xmlns:entry',namespaces):
        for child in item.findall('yt:videoId', namespaces):
            return(child.text)

while True == True:
    videoID =  getLatestVideo(channelID)
    if videoID not in videos:
        videos.append(videoID)
        r = requests.get("https://youtube.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&id=" + videoID + "&key=" + apiKey)
        json = r.json()
        print(json["items"][0]["snippet"]["liveBroadcastContent"])
    else:
        print("no new video")
    time.sleep(60)