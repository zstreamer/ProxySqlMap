import requests,json

class SqlMapApi:
    def __init__(self,sqlurl,url,cookie,referer,data=''):
        self.sqlurl = str(sqlurl)
        self.url = str(url)
        self.cookie = str(cookie)
        self.referer = str(referer)
        self.data = str(data)
    def getTaskId(self):
        taskid = requests.get(url ='http://'+self.sqlurl + '/task/new')
        taskid = json.loads(taskid.text)
        return str(taskid['taskid'])
    def startScan_P(self,taskid):
        start = requests.post(url = "http://"+self.sqlurl + '/scan/' + taskid + '/start',data=json.dumps({"url":self.url,"data":self.data,"referfer":self.referer,"cookie":self.cookie}),headers={"Content-Type":"application/json"})
        if json.loads(start.text)["success"] == True:
            return True
        else:
            return False
    def startScan_G(self,taskid):
        start = requests.post(url = "http://"+self.sqlurl + '/scan/' + taskid + '/start',data=json.dumps({"url":self.url,"referfer":self.referer,"cookie":self.cookie}),timeout=5,headers={"Content-Type":"application/json"})
        if json.loads(start.text)["success"] == True:
            return True
        else:
            return False
    def getStatus(self,taskid):
        r = requests.get(url='http://'+self.sqlurl + taskid + '/status')
        if json.loads(r.text)['success'] == True:
            if json.loads(r.text)['status'] != 'running':
                return True
            else:
                return 'running'
        else:
            return False
    def getData(self,taskid):
        data = json.loads(requests.get(url='http://'+self.sqlurl + taskid + '/data').text)['data']
        if data is None:
            return False
        else:
            return data


'''
taskid = requests.get(url ='http://'+'127.0.0.1:8775' + '/task/new')
taskid = json.loads(taskid.text)['taskid']
print(requests.post(url='http://'+'127.0.0.1:8775/scan/' + taskid + '/start',data=json.dumps({"url":"http://127.0.0.1/1.php","data":"user=1"}),headers={"Content-Type":"application/json"}).text)
while True:
    r = requests.get(url='http://'+'127.0.0.1:8775/scan/' + taskid + '/status')
    print(r.text)
    time.sleep(5)
    if json.loads(r.text)['success'] == True:
        break

print(requests.get(url='http://'+'127.0.0.1:8775/scan/' + taskid + '/data').text)
'''