import tornado.ioloop
import tornado.web
import tornado.process
import time
from jinja2 import Template
from jinja2 import Environment, PackageLoader, FileSystemLoader
import os
import argparse

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
        self.write(jinja_env.get_template('big_render.html').render({}))

class BigRenderHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(jinja_env.get_template('loop_t.html').render({'time':time.time()}))

application = tornado.web.Application([
    (r"/trender", LoopTempHandler),
    (r"/calc", MainHandler),
    (r'/bigrender', BigRenderHandler),
])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='tornado wsgi args.')
    parser.add_argument('--port', dest='port',  
            action='store', type=int, metavar='P', default=6001,
            help='wsgi start port.[default 6001]')
    args = parser.parse_args()
    port = args.port

    application.listen(port)
    tornado.ioloop.IOLoop.instance().start()
