import tornado.ioloop
import tornado.web
import tornado.process
import time

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        t1 = time.time()
        for i in range(100000):
            a = 'a'*100
            b = 'b'*100
            c = a+b
        t2 = (time.time() - t1) * 1000

        self.write("Hello, world from tornado: %s ms"%t2)

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(6001)
    tornado.ioloop.IOLoop.instance().start()
