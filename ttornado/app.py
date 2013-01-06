import tornado.ioloop
import tornado.web
import tornado.process

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world from tornado")

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(6001)
    tornado.ioloop.IOLoop.instance().start()
