import tornado.ioloop
import tornado.web
import tornado.process
import time
from jinja2 import Template
from jinja2 import Environment, PackageLoader, FileSystemLoader
import os

curpath = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(curpath, 'templates')
jinja_env = Environment(loader=FileSystemLoader(templates_dir))

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        t1 = time.time()
        for i in range(100000):
            a = 'a'*100
            b = 'b'*100
            c = a+b
        t2 = (time.time() - t1) * 1000

        self.write("Hello, world from tornado: %s ms"%t2)

class LoopTempHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(jinja_env.get_template('loop_t.html').render({'time':time.time()}))

application = tornado.web.Application([
    (r"/t", LoopTempHandler),
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(6001)
    tornado.ioloop.IOLoop.instance().start()
