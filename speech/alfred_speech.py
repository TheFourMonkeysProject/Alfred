__author__ = 'matt.livingston'

import http.client, urllib.parse, json
import os
import winsound


class AlfredSpeech:
    clientId = "d751385f980f42ed9181a0d8a8235991"
    clientSecret = "25eb075d1acf4cf7857dfe53a38c2007"
    ttsHost = "https://speech.platform.bing.com"
    AccessTokenHost = "oxford-speech.cloudapp.net"
    path = "/token/issueToken"

    params = urllib.parse.urlencode({'grant_type': 'client_credentials', 'client_id': clientId, 'client_secret': clientSecret, 'scope': ttsHost})
    headers = {"Content-type": "application/x-www-form-urlencoded"}

    body_template = """
    <speak version='1.0' xml:lang='en-GB'>
        <voice xml:lang='en-gb' xml:gender='Male' name='Microsoft Server Speech Text to Speech Voice (en-GB, George, Apollo)'>%s
        </voice>
    </speak>
    """


    def get_access_token(self):
        # Connect to server to get the Oxford Access Token
        conn = http.client.HTTPSConnection(self.AccessTokenHost)
        conn.request("POST", self.path, self.params, self.headers)
        response = conn.getresponse()
        #print(response.status, response.reason)

        data = response.read()
        #print(data)
        conn.close()
        accesstoken = data.decode("UTF-8")
        #print("Oxford Access Token: " + accesstoken)

        #decode the object from json
        ddata=json.loads(accesstoken)
        access_token = ddata['access_token']

        return access_token

    def format_text_command(self, text):
        return self.body_template % text

    def clean_up(self):
        os.remove('response.mp3')


    def get_voice_response(self, body):
        headers = {"Content-type": "application/ssml+xml",
                    "X-Microsoft-OutputFormat": "riff-16khz-16bit-mono-pcm",
                    "Authorization": "Bearer " + self.get_access_token(),
                    "X-Search-AppId": "07D3234E49CE426DAA29772419F436CB",
                    "X-Search-ClientID": "d751385f980f42ed9181a0d8a8235991",
                    "User-Agent": "TTSForPython"}

        #Connect to server to synthesize the wave
        conn = http.client.HTTPSConnection("speech.platform.bing.com:443")
        conn.request("POST", "/synthesize", body, headers)
        response = conn.getresponse()
        print(response.status, response.reason)
        data = response.read()
        f = open('response.mp3','wb')
        f.write(data)
        f.close()
        conn.close()

        winsound.PlaySound('response.mp3', winsound.SND_FILENAME)

        self.clean_up()

        #print("The synthesized wave length: %d" %(len(data)))


    def respond(self, command):
        self.get_voice_response(self.format_text_command(command))



#alfred_speech = AlfredSpeech()

#alfred_speech.respond("Good morning sir")

