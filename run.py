from mitmproxy.master import Master
from mitmproxy.proxy import config
from mitmproxy import options
from mitmproxy.proxy.server import ProxyServer
from lib.getHttpClass import filterRq


class ProxyStart():
    def __init__(self,option,obj):
        self.opts = options.Options()
        for i in option:
            self.__addOption(i)
        self.cf = config.ProxyConfig(self.opts)
        self.server = ProxyServer(config=self.cf)
        self.master = Master(opts = self.opts)
        self.master.server = self.server
        self.master.addons.add(obj)
    def __addOption(self,*args):
        self.opts.add_option(args[0][0],args[0][1],args[0][2],args[0][3])
    def run(self):
        self.master.run()


def server_run():
    conf = [('listen_host',str,'127.0.0.1','this is host'),
            ('listen_proxy',int,8080,'this is proxy'),
            ('mode',str,'regular','this is mode'),
            ("body_size_limit",int,100000,"this is response size")]
    start = ProxyStart(conf,filterRq())
    start.run()


if __name__ == '__main__':
    server_run()