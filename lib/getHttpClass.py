from mitmproxy import http
import config,requests
from lib.requestSql import SqlMapApi

class filterRq():
    def request(self,f):
        getHttp(f)

    def response(self,f):
        getHttp(f)

class getHttp():
    def __init__(self,f):
        self.flow = f
        self.header = dict()
        if(str(self.flow.response.headers['Content-Type']).split(';')[0] not in config.ContentType):
            self.header['method'] = self.__getMethod()
            self.header['url'] = self.__getUrl()
            self.header['Referer'] = self.__getReferer()
            self.header['cookie'] = self.__getCookie()
            self.header['Accept'] = self.__getAccept()
            self.header['data'] = self.__getData()
            self.header['Content-Type'] = self.__getContentType()
            res = SqlMapApi(config.sqlmapapi_url,self.header['url'],self.header['cookie'],self.header['Referer'],self.header['data'])
            taskid = res.getTaskId()
            if str(self.header['method']).upper() == 'GET':
                res.startScan_G(taskid)
            else:
                res.startScan_P(taskid)
            print(self.header)
    def __getMethod(self):
        return self.flow.request.method
    def __getUrl(self):
        return self.flow.request.url
    def __getReferer(self):
        if('Referer' in self.flow.request.headers):
            return self.flow.request.headers['Referer']
        else:
            return ''
    def __getCookie(self):
        if('Cookie' in self.flow.request.headers['Cookie']):
            return self.flow.request.headers['Cookie']
        else:
            return ''
    def __getData(self):
        if(str(self.flow.request.method).upper() != 'GET'):
            return bytes(self.flow.request.content).decode('utf-8')
        else:
            return ''
    def __getAccept(self):
        return self.flow.request.headers['Accept']
    def __getContentType(self):
        return self.flow.response.headers['Content-Type']