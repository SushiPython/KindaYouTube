import requests
from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

@app.route('/get-videos')
def videos():
    cont = request.args.get('cont')
    data = ""
    url = "https://www.youtube.com/youtubei/v1/browse?key=apikey"

    headers = {
        "Cookie": "".encode('utf-8'),
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0",
        "Authorization": "SAPISIDHASH auth",
        "X-Goog-Visitor-Id": "visitor-id",
        "X-Goog_AuthUser": "2",
        "TE": "Trailers",
        "X-Youtube-Client-Name": "1",
        "X-Youtube-Client-Version": "2.20210224.06.00",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept": "*/*",
        "Connection": "keep-alive",
        "X-Origin": "https://www.youtube.com"
    }
    
    
    response = requests.post(
        url=url,
        headers=headers,
        data=data
    )

    videoIds = []
    for b in response.json()['onResponseReceivedActions'][0]['appendContinuationItemsAction']['continuationItems']:
        if "continuationItemRenderer" in b:
            videoIds.append(b['continuationItemRenderer']['continuationEndpoint']['continuationCommand']['token'])
        else:
            videoIds.append(b['richItemRenderer']['content']['videoRenderer']['videoId'])
    return " ".join(videoIds)

@app.route('/')
def main():
    return render_template('index.html')

app.run(host='0.0.0.0', port=8080)
