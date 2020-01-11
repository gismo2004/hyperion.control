from .utils import log
import json
import requests 

class Connection:
    def __init__(self):
        self.__headers = {'Content-type': 'application/json'}
        self.__url = "http://127.0.0.1:8090/json-rpc"

    def updateHeader(self, authToken):
        if authToken == "":
            self.__headers.pop('Authorization', 'default')
            return

        self.__headers.update({'Authorization' : 'token '+authToken})

    def updateURL(self, ip, port):
        self.__url = "http://"+ip+":"+str(port)+"/json-rpc"

    def send(self, body):
        try:
            log("Send Request: " + json.dumps(body))
            req = requests.post(url = self.__url, data = json.dumps(body).encode('utf-8'), headers=self.__headers, timeout=5)
            log(req.text)
        except:
            log("Timeout occured for method post2")

    def sendComponentState(self, comp, state):
        body = {"command":"componentstate", "componentstate":{"component": comp, "state": state }, "tan":1}
        self.send(body)

    def sendVideoMode(self, mode):
        body = {"command":"videoMode", "videoMode":mode, "tan":1}
        self.send(body)
